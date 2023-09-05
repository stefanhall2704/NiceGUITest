from nicegui import ui


class Activity:
    def __init__(self, activity):
        self.activity = activity

    def activity_info_section(self) -> None:
        with ui.column():
            ui.link(
                self.activity.title, f"https://localhost/{self.activity.ID}"
            ).classes("text-xl")
            with ui.grid(columns=2):
                if self.activity.jira_work_item:
                    ui.label("Jira Work Item")
                    ui.label(self.activity.jira_work_item)
                ui.label("Risk Level")
                ui.label(self.activity.risk_level)
                ui.label("Team")
                ui.label(self.activity.application_team_id)

    def activity_release_section(self) -> None:
        with ui.column():
            if self.activity.release_id:
                with ui.row():
                    ui.label("Release:")
                    ui.link(
                        self.activity.release.name,
                        f"https://localhost/release/{self.activity.release.ID}",
                    )
                ui.button(
                    icon="touch_app",
                ),

    def get_approval(self, approval_id: int):
        approvals = [
            approval
            for approval in self.activity.approvals
            if approval.release_approval_type_id == approval_id
        ]
        if approvals:
            with ui.icon("checkbox").classes("pl-10"):
                ui.tooltip(
                    f"Approved By 19 on 2021-09-30T15:00:00",
                )
        else:
            ui.button("Approve")

    def activity_approval_section(self) -> None:
        with ui.grid(columns=2):
            ui.label("Testing And User Acceptance")
            self.get_approval(1)

            ui.label("Performance")
            self.get_approval(2)

            ui.label("Regression")
            self.get_approval(3)

            ui.label("Release")
            self.get_approval(4)
