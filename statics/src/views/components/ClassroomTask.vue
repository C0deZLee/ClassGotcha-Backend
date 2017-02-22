<template>
   <div id="vertical-timeline" class="vertical-container light-timeline no-margins">
      <div class="vertical-timeline-block">
         <a data-toggle="modal" data-target="#add-task">
            <div class="vertical-timeline-icon navy-bg" v-show="user_in_classroom">
               <i class="fa fa-star" ></i>
            </div>
         </a>
         <div class="vertical-timeline-content" v-show="user_in_classroom">
            <div class="row">
               <div class="col-md-10">
                  <h2>Add a new task to classroom?</h2>
               </div>
               <div class="col-md-2">
                  <a data-toggle="modal" data-target="#add-task" class=" btn btn-primary"><i class="fa fa-plus"></a>
               </div>
            </div>
         </div>
         <div v-for="task in tasks" class="vertical-timeline-block">
            <!-- 1) Homework 2) Quiz 3) Exam-->            
            <div class="vertical-timeline-icon" :class="{ 'blue-bg': task.category === 1, 'yellow-bg':task.category === 2, 'red-bg': task.category === 3}">
               <i class="fa" :class="{ 'fa-file-text': task.category === 1, 'fa-pencil':task.category === 2, ' fa-warning': task.category === 3}"></i>
            </div>
            <div class="vertical-timeline-content">
               <h2>{{task.task_name}}</h2>
               <p>{{task.description}}
               </p>
               <a @click="changeTaskWindowTriggle(task.id)" v-if="user_in_classroom" class="btn btn-sm btn-white">Edit</a>
               <span class="vertical-date">
               {{taskTime(task, 1)}} <br>
               <small>{{taskTime(task, 2)}}</small>
               </span>
            </div>
         </div>
      </div>
      <div class="modal inmodal fade" id="add-task" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
         <div class="modal-dialog">
            <div class="modal-content">
               <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                  <h4 class="modal-title"><i class="fa fa-tasks"></i> Task Detail</h4>
               </div>
               <div class="modal-body">
                  <div class="row">
                     <div class="col-md-12">
                        <span>Task Type</span>
                        <select class="form-control m-b" v-model="task_category">
                           <option value="1">Assignment</option>
                           <option value="2">Quiz</option>
                           <option value="3">Exam</option>
                           <option value="6">Other</option>
                        </select>
                     </div>
                  </div>
                  <div class="row">
                     <div class="col-md-12">
                        <span>Title</span>
                        <input class="form-control m-b" v-model="task_title" placeholder="eg. Homework 1"></input>
                     </div>
                     <div class="col-md-12" >
                        <input type="radio" v-model="task_subcategory" value="1" id="in-class" name="a">
                        <label for="in-class"></label> Take home 
                        <i class="m-l" ></i>
                        <input type="radio"  v-model="task_subcategory" value="2" id="take-home" name="a">
                        <label for="take-home"></label> In class
                        <i class="m-l" ></i>
                        <input type="radio" v-model="task_subcategory" value="3" id="other-time" name="a">
                        <label for="other-time"></label> <span> Other Time</span>
                     </div>
                     <div class="col-md-12 m-t">
                        <div class="form-group">
                           <span>Time</span>
                           <div class="input-group date">
                              <input type="text" v-show="task_subcategory==1" placeholder="Due time?" v-model="task_due_datetime" id="task-due-datetime" class="form-control" />
                              <input type="text" v-show="task_subcategory==2" placeholder="Which day?" v-model="task_due_date" id="task-due-date" class="form-control" />
                              <input type="text" v-show="task_subcategory==3" placeholder="Start at?" v-model="task_start" id="task-start" class="form-control" />
                              <input type="text" v-show="task_subcategory==3" placeholder="End at?" v-model="task_end" id="task-end" class="form-control" />
                              <span class="input-group-addon">
                              <span class="fa fa-calendar"></span>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-12" v-show="task_subcategory==3">
                        <span>Location</span>
                        <input class="form-control m-b" v-model="task_location" placeholder="eg. Willard Building 123"></input>                  
                     </div>
                     <div class="col-md-12 m-b">
                        <span>Repeat Every</span>
                        <br>
                        <div class="btn-group">
                            <!--TODO: FIXME-->
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Su')? 'active':''" @click="addTaskRepeat('Su')">Su</button>                                    
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Mo')? 'active':''" @click="addTaskRepeat('Mo')">Mo</button>
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Tu')? 'active':''" @click="addTaskRepeat('Tu')">Tu</button>
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('We')? 'active':''" @click="addTaskRepeat('We')">We</button>   
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Th')? 'active':''" @click="addTaskRepeat('Th')">Th</button>
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Fr')? 'active':''" @click="addTaskRepeat('Fr')">Fr</button>
                           <button class="btn btn-white btn-sm" :class="task_repeat.includes('Sa')? 'active':''" @click="addTaskRepeat('Sa')">Sa</button>
                        </div>
                     </div>
                     <div class="col-md-12">
                        <span>Description</span>                         
                        <textarea class="form-control m-b" v-model="task_dscr" placeholder="Describe it in more detail? (optional)"></textarea>
                     </div>
                     <!--<p class="text-center"><a @click="show_more=!show_more"> <i class="fa fa-angle-double-down"></i> More Options </a></p>-->
                     <!--<div class="col-md-12 m-t" v-show="show_more">
                        <span>Add or Upload Related File</span>
                        
                        </div>-->
                  </div>
                  <p v-show="task_errMsg">{{task_errMsg}}</p>
               </div>
               <div class="modal-footer">
                  <a @click="postTask($event)" :disabled="invaild_task" class="btn btn-sm btn-primary">Add To Classroom</a>
               </div>
            </div>
         </div>
      </div>
      <div v-if="chosen_task" class="modal inmodal fade" id="change-task" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
         <div class="modal-dialog">
            <div class="modal-content">
               <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                  <h4 class="modal-title"><i class="fa fa-tasks"></i> Task Detail</h4>
               </div>
               <div class="modal-body">
                  <div class="row">
                     <div class="col-md-12">
                        <span>Task Type</span>
                        <select class="form-control m-b" v-model="chosen_task.category">
                           <option value="1">Assignment</option>
                           <option value="2">Quiz</option>
                           <option value="3">Exam</option>
                           <option value="6">Other</option>
                        </select>
                     </div>
                  </div>
                  <div class="row">
                     <div class="col-md-12">
                        <span>Title</span>
                        <input class="form-control m-b" v-model="chosen_task.task_name"></input>
                     </div>
                     <div class="col-md-12">
                        <div class="form-group">
                           <span>Time</span>
                           <div class="input-group date">
                              <input type="text" v-show="chosen_task.start" placeholder="Start at?" v-model="chosen_task.start" id="chosen-task-start" class="form-control" />
                              <input type="text" v-show="chosen_task.end" placeholder="End at?" v-model="chosen_task.end" id="chosen-task-end" class="form-control" />
                              <span class="input-group-addon">
                              <span class="fa fa-calendar"></span>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-12" v-show="task_subcategory==3">
                        <span>Location</span>
                        <input class="form-control m-b" v-model="chosen_task.location" placeholder="eg. Willard Building 123"></input>                  
                     </div>
                     <div class="col-md-12 m-b">
                        <span>Repeat Every</span>
                        <br>
                        <div class="btn-group">
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Su')? 'active':''" @click="changeTaskRepeat('Su')">Su</button>                                    
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Mo')? 'active':''" @click="changeTaskRepeat('Mo')">Mo</button>
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Tu')? 'active':''" @click="changeTaskRepeat('Tu')">Tu</button>
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('We')? 'active':''" @click="changeTaskRepeat('We')">We</button>    
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Th')? 'active':''" @click="changeTaskRepeat('Th')">Th</button>
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Fr')? 'active':''" @click="changeTaskRepeat('Fr')">Fr</button>                          
                           <button class="btn btn-white btn-sm" :class="chosen_task.repeat.includes('Sa')? 'active':''" @click="changeTaskRepeat('Sa')">Sa</button>
                        </div>
                     </div>
                     <div class="col-md-12">
                        <span>Description</span>                         
                        <textarea class="form-control m-b" v-model="chosen_task.description" placeholder="Describe it in more detail? (optional)"></textarea>
                     </div>
                     <!--<p class="text-center"><a @click="show_more=!show_more"> <i class="fa fa-angle-double-down"></i> More Options </a></p>-->
                     <!--<div class="col-md-12 m-t" v-show="show_more">
                        <span>Add or Upload Related File</span>
                        
                        </div>-->
                  </div>
                  <p v-show="task_errMsg">{{task_errMsg}}</p>
               </div>
               <div class="modal-footer">
                  <a @click="remTask()" class="btn btn-sm btn-danger">Delete</a>                   
                  <a @click="changeTask()" class="btn btn-sm btn-primary">Update</a>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>
<script>
    // import { toUtcString } from 'utils/timeFilter'
    export default {
        name: 'ClassroomTask',
        data() {
            return {
                show_more: false,

                task_category: '1', // 1: homework, 2: quiz, 3: exam, 6:other
                task_subcategory: '1', // 1: take home, 2: in class, 3: other time
                task_location: '',
                task_title: '',
                task_dscr: '',
                task_repeat: '',

                task_due_datetime: null,
                task_due_date: null,
                task_start: null,
                task_end: null,
                task_errMsg: '',

                chosen_task: {
                    repeat: ''
                }
            }
        },
        methods: {
            postTask() {
                /* global Date:true, moment:true */
                if (!this.invaild_task) {
                    let start = ''
                    let end = ''
                    if (this.task_due_date) {
                        start = moment(this.task_due_date, 'MM/DD/YYYY').format('YYYY-MM-DD') + 'T' + this.currnet_classroom.class_time.formatted_start_time
                        end = moment(this.task_due_date, 'MM/DD/YYYY').format('YYYY-MM-DD') + 'T' + this.currnet_classroom.class_time.formatted_end_time
                    } else if (this.task_due_datetime) {
                        end = moment(this.task_due_datetime, 'MM/DD/YYYY hh:mm A').format('YYYY-MM-DDTHH:mm:ss')
                    } else if (this.task_start && this.task_end) {
                        start = moment(this.task_start, 'MM/DD/YYYY hh:mm A').format('YYYY-MM-DDTHH:mm:ss')
                        end = moment(this.task_end, 'MM/DD/YYYY hh:mm A').format('YYYY-MM-DDTHH:mm:ss')
                    }

                    const data = {
                        formData: {
                            task_name: this.task_title,
                            description: this.task_dscr,
                            start: start,
                            end: end,
                            location: this.task_location,
                            category: parseInt(this.task_category),
                            classroom: parseInt(this.$route.params.classroom_id),
                        },
                        pk: this.$route.params.classroom_id
                    }
                    if (this.task_repeat) {
                        data.formData.repeat = this.task_repeat
                        data.formData.repeat_start = this.currnet_classroom.semester.formatted_start_date
                        data.formData.repeat_end = this.currnet_classroom.semester.formatted_end_date
                        console.log('repeat', data)
                    }
                    this.$store.dispatch('postClassroomTask', data)
                    this.clearTask()
                } else {
                    this.task_errMsg = 'Did you miss something?'
                    this.clearTime()
                }
            },
            changeTask() {
                const data = {
                    pk: this.chosen_task.id,
                    formData: this.chosen_task
                }
                this.$store.dispatch('updateTask', data)
            },
            remTask(task) {
                this.$store.dispatch('deleteTask', this.chosen_task.id)

            },
            addTaskRepeat(day) {
                if (this.task_repeat.includes(day))
                    this.task_repeat = this.task_repeat.replace(day, '')
                else
                    this.task_repeat = this.task_repeat + day
            },
            changeTaskRepeat(day) {
                if (this.chosen_task.repeat.includes(day))
                    this.chosen_task.repeat = this.chosen_task.repeat.replace(day, '')
                else
                    this.chosen_task.repeat = this.chosen_task.repeat + day
            },
            clearTask() {
                this.clearTime()
                this.task_subcategory = 1
                this.task_errMsg = ''
                this.task_repeat = ''
                this.task_title = ''
                this.task_dscr = ''
                this.task_location = ''
            },
            clearTime() {
                this.task_due_datetime = null
                this.task_due_date = null
                this.task_start = null
                this.task_end = null
            },
            taskTime(task, type) {
                if (type === 1) {
                    if (task.start) {
                        return moment.utc(task.start).format('LT')
                    } else {
                        return moment.utc(task.end).format('LT')
                    }
                } else if (type === 2) {
                    if (task.start) {
                        return moment.utc(task.start).format('MMM D')
                    } else {
                        return moment.utc(task.end).format('MMM D')
                    }
                }

            },
            changeTaskWindowTriggle(id) {
                for (let i in this.tasks) {
                    if (this.tasks[i].id === id) {
                        this.chosen_task = this.tasks[i]
                        $('#change-task').modal('show')
                    }
                }
            }
        },
        computed: {
            currnet_classroom() {
                return this.$store.getters.currentClassroom
            },
            user_in_classroom() {
                return this.$store.getters.userInClassroom
            },
            tasks() {
                return this.$store.getters.classroomTasks
            },
            invaild_task() {
                if (this.task_title === '')
                    return true
                else if (this.task_subcategory === '1' && !this.task_due_datetime)
                    return true
                else if (this.task_subcategory === '2' && !this.task_due_date)
                    return true
                else if (this.task_subcategory === '3' && !(this.task_start && this.task_end))
                    return true
                else
                    return false
            },
        },
        mounted() {
            /* global $:true */
            // enable all datetime pickers
            $('#task-due-datetime').datetimepicker().on(
                'dp.change', () => { this.task_due_datetime = $('#task-due-datetime').val() }
            )
            $('#task-due-date').datetimepicker({ format: 'L' }).on(
                'dp.change', () => { this.task_due_date = $('#task-due-date').val() }
            )
            $('#task-start').datetimepicker().on(
                'dp.change', () => { this.task_start = $('#task-start').val() }
            )
            $('#task-end').datetimepicker().on(
                'dp.change', () => { this.task_end = $('#task-end').val() }
            )
            $('#chosen-task-start').datetimepicker().on(
                'dp.change', () => { this.task_end = $('#chosen-task-start').val() }
            )
            $('#chosen-task-end').datetimepicker().on(
                'dp.change', () => { this.task_end = $('#chosen-task-end').val() }
            )
        },
        watch: {
            task_subcategory: 'clearTime'
        }
    }

</script>
