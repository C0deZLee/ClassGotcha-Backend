<template>
   <div>
      <div class="row  border-bottom white-bg dashboard-header">
         <div class="col-sm-3">
            <h2 v-show="!show_event_detail && !create_new_event">Recommended Tasks</h2>
            <h2 v-show="show_event_detail">Event Detail</h2>
            <h2 v-show="create_new_event">Create New Event</h2>
            <div class="ibox-content" v-show="!show_event_detail && !create_new_event">
               <div id="external-events">
                  <p>Drag a event and drop into callendar.</p>
                  <div v-for="recommened_task in user_recommened_tasks" class="external-event" :class="eventTaskBg(recommened_task)">{{recommened_task.task_name}} </div>
               </div>
            </div>
            <br>
            <button class="btn form-control m-b" v-show="show_event_detail || create_new_event" @click="show_event_detail=false; create_new_event=false;">Go back to recommended tasks</button>
            <div v-if="show_event_detail">
               <div class="form-group">
                  <label>Event Name</label>
                  <input type="text" class="form-control" placeholder="Title" v-model="event.task_name" disabled>
               </div>
               <div class="form-group" v-show="event.start&&event.end">
                  <div class="row" v-if="event.repeat">
                     <div class="col-md-6">
                        <label>Start</label>
                        <input type="text" class="form-control" :value="event.formatted_start_time" placeholder="Start" disabled>
                     </div>
                     <div class="col-md-6">
                        <label>End</label>
                        <input type="text" class="form-control" :value="event.formatted_end_time" placeholder="End" disabled>
                     </div>
                  </div>
                  <div class="row" v-else>
                    <div class="col-md-12">
                        <label>Start</label>
                        <input type="text" class="form-control m-b" :value="formatTime(event.formatted_start_datetime)" placeholder="Start" disabled>
                     </div>
                     <div class="col-md-12">
                        <label>End</label>
                        <input type="text" class="form-control" :value="formatTime(event.formatted_end_datetime)" placeholder="End" disabled>
                     </div>
                  </div>
               </div>
               <div class="form-group" v-show="(!event.start)&&event.end">
                  <div class="row" v-if="event.repeat">
                     <div class="col-md-12">
                        <label>Due</label>
                        <input type="text" class="form-control" :value="event.formatted_end_time" placeholder="End" disabled>
                     </div>
                  </div>
                  <div class="row" v-else>
                     <div class="col-md-12">
                        <label>Due</label>
                        <input type="text" class="form-control" :value="formatTime(event.formatted_end_datetime)" placeholder="End" disabled>
                     </div>
                  </div>
               </div>
               <div class="form-group">
                  <label>Category</label>
                  <input type="text" class="form-control" placeholder="Category" :value="categoryName(event.category)" :disabled="event.category!==7">
               </div>
               <div class="form-group"  v-if="event.classroom" >
                  <label>Classroom</label>
                  <input type="text" class="form-control" placeholder="Classroom" :value="event.classroom.class_short" :disabled="event.category!==7">
               </div>
               <div class="form-group" v-if="event.group">
                  <label>Group</label>
                  <input type="text" class="form-control" placeholder="Group" :value="event.group"   :disabled="event.category!==7">
               </div>
               <div class="form-group" v-show="event.location">
                  <label>Location</label>
                  <input type="text" class="form-control" placeholder="Location" :value="event.location"   :disabled="event.category!==7">
               </div>
               <div class="form-group" v-if="event.repeat">
                  <label>Repeat</label><br>
                  <div class="btn-group" >
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Su')? 'active':''" @click="addTaskRepeat('Su')">Su</button>    
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Mo')? 'active':''" @click="addTaskRepeat('Mo')">Mo</button>
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Tu')? 'active':''" @click="addTaskRepeat('Tu')">Tu</button>
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('We')? 'active':''" @click="addTaskRepeat('We')">We</button>    
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Th')? 'active':''" @click="addTaskRepeat('Th')">Th</button>
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Fr')? 'active':''" @click="addTaskRepeat('Fr')">Fr</button>                      
                     <button class="btn btn-white btn-sm" :class="event.repeat.includes('Sa')? 'active':''" @click="addTaskRepeat('Sa')">Sa</button>
                  </div>
               </div>
            </div>
            <div v-if="create_new_event">
               <div class="form-group">
                  <label>Event Name</label>
                  <input type="text" class="form-control" placeholder="Title" v-model="new_event.task_name">
               </div>
               <div class="form-group">
                  <div class="row">
                     <div class="col-md-6">
                        <label>Start date</label>
                        <input type="text" class="form-control" v-model="new_event.start_date" placeholder="Start">
                     </div>
                     <div class="col-md-6">
                        <label>Start time</label>
                        <input type="text" class="form-control" v-model="new_event.start_time" placeholder="Start">
                     </div>
                     <div class="col-md-6">
                        <label>End date</label>
                        <input type="text" class="form-control" v-model="new_event.end_date" placeholder="End">
                     </div>
                    <div class="col-md-6">
                        <label>End time</label>
                        <input type="text" class="form-control" v-model="new_event.end_time" placeholder="End">
                     </div>
                  </div>
               </div>
               <div class="form-group">
                  <label>Location</label>
                  <input type="text" class="form-control" placeholder="Location" v-model="new_event.location">
               </div>
               <div class="form-group">
                  <label>Repeat</label><br>
                  <div class="btn-group" >
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Su')? 'active':''" @click="addNewTaskRepeat('Su')">Su</button>    
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Mo')? 'active':''" @click="addNewTaskRepeat('Mo')">Mo</button>
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Tu')? 'active':''" @click="addNewTaskRepeat('Tu')">Tu</button>
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('We')? 'active':''" @click="addNewTaskRepeat('We')">We</button>    
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Th')? 'active':''" @click="addNewTaskRepeat('Th')">Th</button>
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Fr')? 'active':''" @click="addNewTaskRepeat('Fr')">Fr</button>                      
                     <button class="btn btn-white btn-sm" :class="new_event.repeat.includes('Sa')? 'active':''" @click="addNewTaskRepeat('Sa')">Sa</button>
                  </div>
               </div>
               <div class="form-group">
                   <button class="btn btn-primary btn-block" @click="postNewTask()">Create</button>
               </div>
            </div>
         </div>
         <div class="col-sm-9">
            <div ref="calendar" id="calendar" ></div>
         </div>
      </div>
      <div class="modal inmodal fade" id="event-detail" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
         <div class="modal-dialog">
            <div class="modal-content">
               <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                  <h4 class="modal-title"><i class="fa fa-clock-o"></i> Event Detail</h4>
               </div>
            </div>
            <div class="modal-footer">
               <button type="button" class="btn btn-white" data-dismiss="modal">Close</button>
               <button type="button" class="btn btn-primary">Save changes</button>
            </div>
         </div>
      </div>
   </div>
   </div>
</template>
<script>
    export default {
        data() {
            return {
                // event
                // selected event
                event: {
                    // type: 0, // Event
                    // formatted_start_time: '',
                    // formatted_start_date: '',
                    // formatted_end_date: '',
                    // category: 7, // Other
                    // formatted_end_time: '',
                    // description: '',
                    // id: '',
                    // location: '',
                    // repeat_list: [],
                    // start: '',
                    // task_name: '',
                },
                new_event: {
                    task_name: '',
                    type: 0, // Event
                    start_time: '',
                    start_date: '',
                    start: '',
                    end_time: '',
                    end_date: '',
                    end: '',
                    category: 6, // Other
                    description: '',
                    location: '',
                    repeat: '',
                },
                // created_event: {},
                // for fullcalendar
                events: [],
                event_sources: [],
                // category dictionary
                category_choices: {
                    0: { name: 'Class' },
                    1: { name: 'Homework' },
                    2: { name: 'Quiz' },
                    3: { name: 'Exam' },
                    4: { name: 'Todo' },
                    5: { name: 'Group Meeting' },
                    6: { name: 'Other' }
                },
                // calendar settings
                calendar_header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay,listWeek'
                },
                sync: false,
                // UI triggers
                show_event_detail: false,
                create_new_event: false

            }
        },
        methods: {
            createEvents() {
                let event_sources_list = [
                    // {
                    // events: []
                    // color: ''
                    // }
                ]
                let event_list0 = [] // classes
                let event_list1 = [] // homework
                let event_list2 = [] // quiz
                let event_list3 = [] // exam
                let event_list7 = [] // other
                const event_color0 = '#1ab394'
                const event_color1 = '#f8ac59'
                const event_color2 = '#ed5565'
                const event_color3 = '#ed5565'
                const event_color7 = '#23c6c8'
                for (let i in this.user_tasks) {
                    const task = this.user_tasks[i]
                    /* global moment:true */
                    // classes
                    if (task.category === 0) {
                        event_list0.push({
                            id: task.id,
                            title: task.task_name + '\n' + task.location,
                            editable: false,
                            start: task.formatted_start_time,
                            end: task.formatted_end_time,
                            dow: task.repeat_list,
                            repeat: [{
                                start: task.formatted_start_date,
                                end: task.formatted_end_date
                            }]
                        })
                    }
                    // homework
                    else if (task.category === 1) {
                        let homework = {
                            id: task.id,
                            title: task.task_name,
                            editable: false,
                            start: moment.utc(task.end).add(-0.5, 'hours').format(),
                            end: task.end,
                        }
                        if (task.repeat_list.length) {
                            homework.dow = task.repeat_list
                            homework.start = moment.utc(task.formatted_end_time, 'HH:mm:ss').add(-0.5, 'hours').format('HH:mm:ss')
                            homework.end = task.formatted_end_time
                            console.log(homework)
                        }
                        event_list1.push(homework)

                    }
                    // quiz
                    else if (task.category === 2) {
                        event_list2.push({
                            id: task.id,
                            title: task.task_name,
                            editable: false,
                            start: (task.start ? task.start : task.end),
                            end: (task.start ? task.end : moment.utc(task.end).add(0.5, 'hours').format()),
                        })
                    }
                    // exam
                    else if (task.category === 3) {
                        event_list3.push({
                            id: task.id,
                            title: (task.location ? task.task_name + '\n' + task.location : task.task_name),
                            editable: false,
                            start: (task.start ? task.start : task.end),
                            end: (task.start ? task.end : moment.utc(task.end).add(0.5, 'hours').format()),

                        })
                    } else if (task.category === 6) {
                        event_list7.push({
                            id: task.id,
                            title: (task.location ? task.task_name + '\n' + task.location : task.task_name),
                            editable: true,
                            start: (task.start ? task.start : task.end),
                            end: (task.start ? task.end : moment.utc(task.end).add(0.5, 'hours').format()),

                        })
                    }
                }
                event_sources_list.push({ events: event_list0, color: event_color0 })
                event_sources_list.push({ events: event_list1, color: event_color1 })
                event_sources_list.push({ events: event_list2, color: event_color2 })
                event_sources_list.push({ events: event_list3, color: event_color3 })
                event_sources_list.push({ events: event_list7, color: event_color7 })

                this.event_sources = event_sources_list
            },
            createExternalEvents() {
                /* global $:true */
                $('#external-events div.external-event').each(function() {
                    // store data so the calendar knows to render an event upon drop
                    $(this).data('event', {
                        title: $.trim($(this).text()), // use the element's text as the event title
                        stick: true // maintain when user navigates (see docs on the renderEvent method)
                    })
                    // make the event draggable using jQuery UI
                    $(this).draggable({
                        zIndex: 10,
                        revert: true, // will cause the event to go back to its
                        revertDuration: 1 //  original position after the drag
                    })

                })
            },
            postNewTask() {
                let formData = this.new_event
                formData.start = formData.start_date + 'T' + formData.start_time
                formData.end = formData.end_date + 'T' + formData.end_time
                formData.involved = [this.user.id]
                if (!formData.repeat) {
                    delete formData['repeat']
                }
                this.$store.dispatch('postTask', formData)
                    .then(() => {
                        this.create_new_event = false
                        this.$store.dispatch('getTasks').then(() => {
                            this.createEvents()
                        })
                    })
            },
            // data formatter
            formatTime(time) {
                /* global moment: true */
                return moment.utc(time).format('l LT')
            },
            // look up method
            categoryName(id) {
                if (this.category_choices[id])
                    return this.category_choices[id].name
                else return null
            },
            // data control
            addTaskRepeat(day) {
                if (this.event.repeat.includes(day))
                    this.event.repeat = this.event.repeat.replace(day, '')
                else
                    this.event.repeat = this.event.repeat + day
            },
            addNewTaskRepeat(day) {
                if (this.new_event.repeat.includes(day))
                    this.new_event.repeat = this.new_event.repeat.replace(day, '')
                else
                    this.new_event.repeat = this.new_event.repeat + day
            },
            // UI control
            eventTaskBg(event) {
                // Homewrok
                if (event.category === 1) {
                    return 'bg-warning'
                }
                // Quiz
                else if (event.category === 2) {
                    return 'bg-danger'
                }
                // Exam
                else if (event.category === 3) {
                    return 'bg-danger'
                }
            },
        },
        computed: {
            user() {
                return this.$store.getters.me
            },
            user_tasks() {
                return this.$store.getters.userTasks
            },
            user_recommened_tasks() {
                return this.$store.getters.userRecommendedTasks
            },
            windowHeight() {
                return window.innerHeight
            }
        },
        created() {
            this.createEvents()
        },
        mounted() {
            /* global $:true */
            const cal = $('#calendar')
            const self = this

            cal.fullCalendar({
                scrollTime: '07:30:00',
                droppable: true,
                // ignoreTimezone: false,
                header: this.calendar_header,
                defaultView: 'agendaWeek',
                editable: true,
                selectable: true,
                selectHelper: true,
                aspectRatio: 1.3,
                timeFormat: 'HH:mm',
                events: self.events,
                eventSources: self.event_sources,
                nowIndicator: true,
                unselectAuto: false,

                // eventRender(event, element) {
                //     if (this.sync) {
                //         self.events = cal.fullCalendar('clientEvents')
                //     }
                // },
                // eventDestroy(event) {
                //     if (this.sync) {
                //         self.events = cal.fullCalendar('clientEvents')
                //     }
                // },
                eventClick(event) {
                    console.log(event)

                    // The following code did this:
                    // When click a event, if the event id is found in self.user_tasks, show event
                    // else, this is a new event, create it
                    let found = false
                    for (let i in self.user_tasks) {
                        if (self.user_tasks[i].id === event.id) {
                            self.event = self.user_tasks[i]
                            found = true
                            self.show_event_detail = true
                            self.create_new_event = false

                        }
                    }
                    if (!found) {
                        self.new_event.task_name = event.title
                        // Here I'm doing the hack, 
                        // fullcalendar event has a start attribute with an 
                        // So I'm constructing time from this
                        const event_start_iso_string = event.start._d.toISOString()
                        const event_start = moment.utc(event_start_iso_string)
                        let event_end
                        if (event.end) {
                            event_end = moment.utc(event.end._d.toISOString())
                        } else {
                            // default length of the event is 2 hours 
                            event_end = moment.utc(event_start_iso_string).add(2, 'hours')
                        }
                        console.log(event.end, event_start, event_end)

                        self.new_event.start_date = event_start.format('YYYY-MM-DD')
                        self.new_event.start_time = event_start.format('HH:mm:ss')
                        self.new_event.end_date = event_end.format('YYYY-MM-DD')
                        self.new_event.end_time = event_end.format('HH:mm:ss')
                        self.show_event_detail = false
                        self.create_new_event = true
                    }
                    // $('#event-detail').modal('show')
                    $(self.$el).trigger('event-selected', event)
                },
                // eventResize(event) {
                //     $(self.$el).trigger('event-resize', event)
                //     self.event = event
                //     self.show_event_detail = true
                // },
                // eventReceive(event) {
                //     $(this).remove()
                //     console.log(event)
                //     self.event = event
                //     self.show_event_detail = true
                // },
                // select(start, end, jsEvent) {
                //     $(self.$el).trigger('event-created', {
                //         start,
                //         end,
                //         allDay: !start.hasTime() && !end.hasTime(),
                //     })
                // },
            })
            this.createExternalEvents()
        },
        watch: {
            events: {
                deep: true,
                handler(val) {
                    $(this.$el).fullCalendar('rerenderEvents')
                },
            }
        },
        events: {
            'remove-event' (event) {
                $(this.$el).fullCalendar('removeEvents', event.id)
            },
            'rerender-events' (event) {
                $(this.$el).fullCalendar('rerenderEvents')
            },
            'refetch-events' (event) {
                $(this.$el).fullCalendar('refetchEvents')
            },
            'render-event' (event) {
                $(this.$el).fullCalendar('renderEvent', event)
            },
            'reload-events' () {
                $(this.$el).fullCalendar('removeEvents')
                $(this.$el).fullCalendar('addEventSource', this.events)
            },
            'rebuild-sources' () {
                $(this.$el).fullCalendar('removeEvents')
                this.eventSources.map(event => {
                    $(this.$el).fullCalendar('addEventSource', event)
                })
            },
        },

    }

</script>
<style>
    /* FULLCALENDAR */
    
    .fc-time-grid .fc-slats td {
        height: 2.5em;
        border-bottom: 0;
    }
    
    .fc-ltr .fc-time-grid .fc-event-container {
        margin: 0 2px;
    }
    
    .fc-event {
        border-radius: 1px
    }
    
    .fc-state-default {
        background-color: #ffffff;
        background-image: none;
        background-repeat: repeat-x;
        box-shadow: none;
        color: #333333;
        text-shadow: none;
    }
    
    .fc-state-default {
        border: 1px solid;
    }
    
    .fc-button {
        color: inherit;
        border: 1px solid #e7eaec;
        cursor: pointer;
        display: inline-block;
        height: 1.9em;
        line-height: 1.9em;
        overflow: hidden;
        padding: 0 0.6em;
        position: relative;
        white-space: nowrap;
    }
    
    .fc-state-active {
        background-color: #1ab394;
        border-color: #1ab394;
        color: #ffffff;
    }
    
    .fc-header-title h2 {
        font-size: 16px;
        font-weight: 600;
        color: inherit;
    }
    
    .fc-content .fc-widget-header,
    .fc-content .fc-widget-content {
        border-color: #e7eaec;
        font-weight: normal;
    }
    
    .fc-border-separate tbody {
        background-color: #F8F8F8;
    }
    
    .fc-state-highlight {
        background: none repeat scroll 0 0 #FCF8E3;
    }
    
    .external-event {
        padding: 5px 10px;
        border-radius: 2px;
        cursor: pointer;
        margin-bottom: 5px;
    }
    
    .fc-ltr .fc-event-hori.fc-event-end,
    .fc-rtl .fc-event-hori.fc-event-start {
        border-radius: 2px;
    }
    
    .fc-event,
    .fc-agenda .fc-event-time,
    .fc-event a {
        padding: 4px 6px;
        background-color: #23c6c8;
        /* background color */
        border-color: #23c6c8;
        /* border color */
    }
    
    .fc-event {
        border: 0px;
        border-left: 5px solid #23c6c8;
    }
    
    .fc-event-time,
    .fc-event-title {
        color: #717171;
        padding: 0 1px;
    }
    
    .ui-calendar .fc-event-time,
    .ui-calendar .fc-event-title {
        color: #fff;
    }
    
    .fc-agenda-view .fc-day-grid .fc-row {
        min-height: 1.5em;
    }

</style>
