<template>
    <div ref:"calendar" id="calendar"></div>
</template>

<script>
    export default {
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
                        right: 'month,agendaWeek,agendaDay'
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
                scrollTime: '07:00:00',
                droppable: true,
                // ignoreTimezone: false,
                header: this.header,
                defaultView: this.defaultView,
                editable: this.editable,
                selectable: this.selectable,
                selectHelper: this.selectHelper,
                aspectRatio: 2,
                timeFormat: 'HH:mm',
                events: self.events,
                eventSources: self.eventSources,

                drop() {
                    $(this).remove()
                },

                eventRender(event, element) {
                    if (this.sync) {
                        self.events = cal.fullCalendar('clientEvents')
                    }
                },

                eventDestroy(event) {
                    if (this.sync) {
                        self.events = cal.fullCalendar('clientEvents')
                    }
                },

                eventClick(event) {
                    $(self.$el).trigger('event-selected', event)
                },

                eventDrop(event) {
                    $(self.$el).trigger('event-drop', event)
                },

                eventResize(event) {
                    $(self.$el).trigger('event-resize', event)
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
        background-color: #1ab394;
        /* background color */
        border-color: #1ab394;
        /* border color */
    }
    
    .fc-event {
        border: 0px;
        border-left: 5px solid #1ab394;
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
