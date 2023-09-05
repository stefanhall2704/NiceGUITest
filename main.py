import json
from nicegui import ui
from fastapi import Depends
from activity import Activity
from task import Task
from src.routers.api.teams import get_activities_for_team
from src.utils.dependencies import get_database


with open("activity.json") as jsonfile:
    activity_data = json.load(jsonfile)


def build_activity_card(activity: Activity) -> None:
    with ui.card().classes("w-full"), ui.card_section().classes("w-full"):
        with ui.row().classes("justify-between"):
            activity.activity_info_section()
            activity.activity_release_section()
            activity.activity_approval_section()
        with ui.expansion("Tasks", icon="work").classes("w-full"):
            for task_data in activity.tasks:
                task = Task(task_data)
                with ui.card().classes("w-full"), ui.card_section().classes("w-full"):
                    with ui.row().classes("justify-between"):
                        ui.separator()
                        ui.label(task.activity.release_activity_task.title)
                        task.task_description()
                        task.stage_board()

database = Depends(get_database)
activites = get_activities_for_team(database=database, team_id="4")
for activities in activites:
    activity = Activity(activity_data)
    build_activity_card(activity)

ui.dark_mode().enable()
ui.run(port=4832)
