import json
from nicegui import ui
from activity import Activity
from task import Task

with open("activity.json") as jsonfile:
    activity_data = json.load(jsonfile)


def build_activity_card(activity: Activity) -> None:
    with ui.card().classes("w-full"), ui.card_section().classes("w-full"):
        with ui.row().classes("justify-between"):
            activity.activity_info_section()
            activity.activity_release_section()
            activity.activity_approval_section()
        with ui.expansion("Tasks", icon="work").classes("w-full"):
            for task_data in activity.activity["tasks"]:
                task = Task(task_data)
                with ui.card().classes("w-full"), ui.card_section().classes("w-full"):
                    with ui.row().classes("justify-between"):
                        ui.separator()
                        ui.label(task.activity["title"])
                        task.task_description()
                        task.stage_board()


for _ in range(10):
    activity = Activity(activity_data)
    build_activity_card(activity)

ui.dark_mode().enable()
ui.run(port=4832)
