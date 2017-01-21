<template>
  <nav class="navbar-default navbar-static-side" role="navigation">
      <div class="sidebar-collapse">
          <ul side-navigation class="nav metismenu" id="side-menu">
              <li class="nav-header">
                  <div class="dropdown profile-element">
                      <!-- Picture of user -->
                      <img alt="image" class="img-circle" src="../img/profile_small.jpg"/>
                      <a class="dropdown-toggle" href>
                              <span class="clear">
                                  <span class="block m-t-xs">
                                      <span data-ng-bind="user.username"></span>
                               </span>
                              </span>
                      </a>
                      <ul class="dropdown-menu animated fadeInRight m-t-xs">
                          <li><a ui-sref="profile">Profile</a></li>
                          <li><a ui-sref="contacts">Contacts</a></li>
                          <li><a ui-sref="inbox">Mailbox</a></li>
                          <li class="divider"></li>
                          <li><a href="../login.html">Logout</a></li>
                      </ul>
                  </div>
                  <div class="logo-element">
                      CG
                  </div>
              </li>
              <li>
                  <a href="/#/">
                      <i class="fa fa-th-large"></i>
                      <span class="nav-label">Index</span>
                  </a>
              </li>

              <li class="active">
                <a href="/#/classroom"><i class="fa fa-laptop"></i> <span class="nav-label">Classroom</span><span class="fa arrow"></span></a>
                <ul class="nav nav-second-level collapse in">
                    <li><a href="/#/classroom/add">+ Add New</a></li>
                     <li><a href="/#/classroom/id/demo">CS 311 (demo)</a></li>
                     <li v-for="classroom in $root.classrooms">
                         <a :href="classroom_url(classroom.id)">{{classroom.class_short}}</a>
                     </li>
                </ul>
            </li>
              <li>
                  <a href="/#/chatroom/id/1">
                      <i class="fa fa-laptop"></i>
                      <span class="nav-label">Chat</span>
                  </a>
              </li>
              <li>
                  <a href="/#/upload/">
                     <i class="fa fa-laptop"></i>
                     <span class="nav-label">Upload</span>
                  </a>
              </li>
              <!-- menu servies start here -->

              <!-- <li
                  ng-repeat="item in menu.items | orderBy: 'position'"
                  ng-if="item.shouldRender(authentication.user);"
                  ng-switch="item.type"
                  ng-class="{ active: location.path().includes(item.state) }"
              >
                  <a ng-switch-when="dropdown">
                      <i class="fa {{item.iconClass}}"></i>
                      <span class="nav-label">{{item.title}}</span>
                      <span class="fa arrow"></span>
                  </a>
                  <ul
                      ng-switch-when="dropdown"
                      class="nav nav-second-level"
                      ng-class="{in: location.path().includes(item.state) }"
                  >
                       Here is the subitem
                      <li
                          role="presentation"
                          ng-repeat="subitem in item.items | orderBy: 'position'"
                          ng-if="subitem.shouldRender(authentication.user);"
                          ui-sref-active="active"
                      >
                          <a
                              ui-sref="{{subitem.state}}"
                              role="menuitem"
                              tabindex="-1"
                              ng-bind="subitem.title"
                          ></a>
                      </li>
                  </ul>

                  <a
                      ng-switch-default
                      ui-sref="{{item.state}}"
                  >
                      <i class="fa {{item.iconClass}}"></i>
                      <span class="nav-label">{{item.title}}</span>
                  </a>

              </li> -->
          </ul>
      </div>
  </nav>
</template>

<script>
  export default {
    name: 'sidebar',
    methods: {
      classroom_url: function(id) {
        return '/#/classroom/id/' + id
      }
    }
  }
</script>