app = angular.module 'order.static', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.orders = []
    $http.get('/shipping/order-list').then (result) ->
        angular.forEach result.data, (item) ->
            $scope.orders.push item
]