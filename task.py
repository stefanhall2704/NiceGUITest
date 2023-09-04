from nicegui import ui
from activity import Activity


class Task(Activity):
    def __init__(self, task_data: dict):
        super().__init__(task_data["release_activity_task"])

    def task_description(self) -> None:
        with ui.column():
            if self.activity["description"]:
                with ui.grid(columns=1):
                    ui.label("Description:")
                    ui.label(self.activity["description"])

    def stage_board(self) -> None:
        stage_status = self.activity.get("stage_status", "Not Specified")
        with ui.column():
            ui.label(f"Stage Status: {stage_status}")

        if stage_status == "Not Started":
            ui.button("Start Stage Task")
        elif stage_status == "In Progress":
            ui.button("Complete Stage Task")
        else:
            with ui.icon("checkbox").classes("text-green-500"):
                ui.tooltip(
                    f"Complete By Stefan Hall on 2021-09-30T15:00:00",
                )
