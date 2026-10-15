"""Add-On that changes the visibility of the running user's notes on selected or queried documents."""
import time
import sys
from documentcloud.addon import SoftTimeOutAddOn


class ChangeNoteVisibility(SoftTimeOutAddOn):
    """Bulk changes visibility of the running user's notes on the selected documents."""

    def main(self):
        """Sets every note owned by the running user to the specified access level."""
        self.client.session.headers.update({"User-Agent": "Change Note Visibility Add-On"})
        access_level = self.data["access_level"]
        accepted_values = ["private", "public", "organization"]
        if access_level not in accepted_values:
            self.set_message("You set an invalid access level. Try again.")
            sys.exit(1)

        user_id = self.client.users.get("me").id
        changed = 0
        unchanged = 0
        skipped = 0
        for document in self.get_documents():
            for note in document.notes:
                # Only touch notes the running user created
                if note.user != user_id:
                    skipped += 1
                    continue
                if note.access == access_level:
                    unchanged += 1
                    continue
                note.access = access_level
                note.save()
                changed += 1
                time.sleep(1)

        self.set_message(
            f"Changed {changed} of your notes to {access_level}; "
            f"{unchanged} were already {access_level}; "
            f"skipped {skipped} notes owned by others."
        )


if __name__ == "__main__":
    ChangeNoteVisibility().main()
