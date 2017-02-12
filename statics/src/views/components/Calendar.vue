<template>
<div>

    <div ref="calendar" id="calendar" ></div>
    <div class="modal inmodal fade" id="event-detail" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                    <h4 class="modal-title"><i class="fa fa-clock-o"></i> Event Detail</h4>
                </div>
                <div class="modal-body">
                 <div class="form-group">
                     <label>Event Name</label>
                  <input type="text" class="form-control" placeholder="Title" v-model="event.task_name" :disabled="event.category===0">
              </div>
              <div class="form-group">
                  <label>Location</label>
                  <input type="text" class="form-control" placeholder="Location" v-model="event.location"   :disabled="event.category===0">
              </div>
              <div class="form-group">
                  <div class="row">
                      <div class="col-md-6">
                  <label>Start</label>
                  <input  type="text" class="form-control" v-model="event.formatted_start_time" placeholder="Start" :disabled="event.category===0">
                      </div>
                      <div class="col-md-6">
                      
                  <label>End</label>
                  <input type="text" class="form-control" v-model="event.formatted_end_time" placeholder="End" :disabled="event.category===0">
                      </div>
                  </div>
              </div>
              <div class="form-group">
                   <label>Repeat</label>
                  <input type="text" class="form-control" placeholder="Location" v-model="event.location"   :disabled="event.category===0">
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
                event: {
                    type: 0, // Event
                    formatted_start_time: '',
                    formatted_start_date: '',
                    formatted_end_date: '',
                    end: '',
                    category: 0, // Class
                    formatted_end_time: '',
                    description: '',
                    id: '',
                    location: '',
                    repeat_list: [],
                    start: '',
                    task_name: '',
                }
            }
        },
        props: {
            events: {
                default () { return [] },
            },

            eventSources: {
                default () { return [] },
            },

            editable: {
                default () { return true },
            },

            selectable: {
                default () { return true },
            },

            selectHelper: {
                default () { return true },
            },

            header: {
                default () {
                    return {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay,listWeek'
                    }
                },
            },

            defaultView: { default () { return 'agendaWeek' }, },

            sync: {
                default () { return false }
            },
        },

        mounted() {
            /*
            global $:true
            */
            const cal = $(this.$el)
            const self = this

            cal.fullCalendar({
                scrollTime: '07:30:00',
                droppable: true,
                // ignoreTimezone: false,
                header: this.header,
                defaultView: this.defaultView,
                editable: this.editable,
                selectable: this.selectable,
                selectHelper: this.selectHelper,
                aspectRatio: 1.3,
                timeFormat: 'HH:mm',
                events: self.events,
                eventSources: self.eventSources,
                nowIndicator: true,
                unselectAuto: false,

                drop() {
                    $(this).remove()
                    $('#event-detail').modal('show')
                },

                eventRender(event, element) {
                    if (this.sync) {
                        self.events = cal.fullCalendar('clientEvents')
                    }
                },
                // eventAfterRender(event, element) {
                //     $('#event-detail').modal('show')
                // },
                eventDestroy(event) {
                    if (this.sync) {
                        self.events = cal.fullCalendar('clientEvents')
                    }
                },

                eventClick(event) {
                    for (let i in self.userTasks) {
                        if (self.userTasks[i].id === event.id)
                            self.event = self.userTasks[i]
                    }
                    $('#event-detail').modal('show')
                    $(self.$el).trigger('event-selected', event)
                },

                eventDrop(event) {
                    $(self.$el).trigger('event-drop', event)
                    $('#event-detail').modal('show')

                },
                eventResize(event) {
                    $(self.$el).trigger('event-resize', event)
                    $('#event-detail').modal('show')

                },
                eventDragStop(event) {
                    $('#event-detail').modal('show')
                },
                select(start, end, jsEvent) {
                    $(self.$el).trigger('event-created', {
                        start,
                        end,
                        allDay: !start.hasTime() && !end.hasTime(),
                    })
                },
            })
        },

        watch: {
            events: {
                deep: true,
                handler(val) {
                    $(this.$el).fullCalendar('rerenderEvents')
                },
            }
        },
        computed: {
            userTasks() {
                return this.$store.getters.userTasks
            },
            windowHeight() {
                return window.innerHeight - 100
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
