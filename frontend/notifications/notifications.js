'use strict';

/**
 * @ngdoc function
 * @name hfosFrontendApp.controller:notificationsCtrl
 * @description
 * # notificationsCtrl
 * Controller of the hfosFrontendApp
 */

class notifications {

    constructor(scope, rootscope, schemata, $modal, user, objectproxy, socket, menu) {
        this.scope = scope;
        this.rootscope = rootscope;
        this.$modal = $modal;
        this.user = user;
        this.op = objectproxy;
        this.socket = socket;
        this.menu = menu;
    }
}

notifications.$inject = ['$scope', '$rootScope', 'schemata', '$modal', 'user', 'objectproxy', 'socket', 'menu', 'NgTableParams'];

export default notifications;
