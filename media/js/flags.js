/// <reference path="../../typings/jquery/jquery.d.ts"/>
/* global angular */
angular.module('FlagsApp', ['tagged.directives.infiniteScroll'])
.config(function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.controller('FlagsController', ['$scope', '$http', '$timeout', function($scope, $http, $timeout) {

    $scope.flags = [];
    $scope.fetchingDisabled = true;
    $scope.next = false;
    $scope.showNext = false;
    $scope.showPrev = false;

    function addFlags() {
        for (var i = 0; i < $scope.data.flags.length; i++) {
            if (isDupe($scope.data.flags[i]))
                continue;
            var flag = angular.copy($scope.data.flags[i]);
            flag['author'] = '';
            if (flag['name'] != '' && flag['location'] != '')
                flag['author'] = flag['name'] + ', ' + flag['location'];
            else if (flag['name'] != '' && flag['location'] == '')
                flag['author'] = flag['name'];
            else if (flag['name'] == '' && flag['location'] != '')
                flag['author'] = flag['location'];

            $scope.flags.push(flag);
        }
    };

    $scope.prepShow = function(flag) {
        var index = findFlagById(flag.id);

        var previous = -1;
        for (var i = index - 1; i >= 0; i--)
            if ($scope.flags[i].image !== '') {
                previous = i;
                break;
            }

        var next = $scope.flags.length + 1;
        for (var i = index + 1; i < $scope.flags.length; i++)
            if ($scope.flags[i].image !== '') {
                next = i;
                break;
            }

        if (previous < 0)
            $scope.showPrevious = false;
        else {
            $scope.showPrevious = $scope.flags[previous];
        }
        if (next >= $scope.flags.length)
            $scope.showNext = false;
        else {
            $scope.showNext = $scope.flags[next];
        }

        $scope.showFlag = flag;
        console.log(previous, index, next);
    };

    function isDupe(index) {
        for (var i = 0; i < $scope.flags.length; i++) {
            if ($scope.flags[i]['id'] == index)
                return true;
        }

        return false;
    };

    function findFlagById(index) {
        for (var i = 0; i < $scope.flags.length; i++) {
          if ($scope.flags[i]['id'] == index)
              return i;
        }
        return null;
    };

    $scope.previewModal = function(flag) {
        $scope.prepShow(flag);
        $("#contentForm").modal('show');
    };

    $scope.flagFlag = function(id) {
        var flag = $scope.flags[findFlagById(id)];
        if (flag.flagReason != '') {
            $http.post('/flag', { 'flagId': flag.id, 'reason': flag.flagReason })
            .success(function(data) {
                $scope.flags[findFlagById(data.id)] = data;
            });
        }
    };

    $scope.loadMore = function() {
        $scope.fetching = true;
        var param = '1';
        if ($scope.data) {
            param = (Number($scope.data.page) + 1).toString();
            if ($scope.data.next == false)
                return;
        }
        $http.get('/pages/' + param + '.json')
        .success(function(data) {
            $scope.data = data;
            addFlags();
            if (!data.next)
                $scope.fetchingDisabled = true;
            else
                $scope.fetchingDisabled = false;
            $timeout(function(){$scope.fetching = false;}, 1000);
        });
    };

    $scope.loadMore();
}]);

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['angular'], factory);
  } else {
    // Browser globals
    root.taggedInfiniteScroll = factory(root.angular);
  }
}(this, function (angular) {
  "use strict";

  // Allows a container to support infinite scroll
  // Based on: http://binarymuse.github.io/ngInfiniteScroll/
  var module = angular.module('tagged.directives.infiniteScroll', []);

  module.directive('taggedInfiniteScroll', ['$window', '$timeout', function($window, $timeout) {
    return {
      scope: {
        callback: '&taggedInfiniteScroll',
        distance: '=taggedInfiniteScrollDistance',
        disabled: '=taggedInfiniteScrollDisabled',
        flagCount: '=taggedInfiniteScrollFlagCount'
      },
      link: function(scope, elem, attrs) {
        var win = angular.element($window);

        var onScroll = function(oldValue, newValue) {
          $('#header').offset({ left: $(window).scrollLeft() + 10 });
          // Do nothing if infinite scroll has been disabled
          if (scope.disabled) {
            return;
          }
          var flagCount = parseInt(scope.flagCount);
          if (isNaN(flagCount))
            flagCount = 0;
          var windowWidth = $window.innerWidth;
          var remaining = 500 + 243 * flagCount - windowWidth - $(window).scrollLeft();
          var shouldGetMore = remaining < 0;

          if (shouldGetMore) {
            $timeout(scope.callback);
          }
        };

        // Check immediately if we need more items upon reenabling.
        scope.$watch('disabled', function(isDisabled){
            if (false === isDisabled) onScroll();
        });

        win.bind('scroll', onScroll);

        // Remove window scroll handler when this element is removed.
        scope.$on('$destroy', function() {
          win.unbind('scroll', onScroll);
        });

        // Check on next event loop to give the browser a moment to paint.
        // Otherwise, the calculations may be off.
        $timeout(onScroll);
      }
    };
  }]);

  // Just return a value to define the module export.
  // This example returns an object, but the module
  // can return a function as the exported value.
  return module;
}));
