"""
This is an Add-On that allows you to change the visibility of all notes queried or selected.
"""
import time
import sys
from documentcloud.addon import SoftTimeOutAddOn


class ChangeNoteVisibility(SoftTimeOutAddOn):
    """Bulk changes visibility of notes on documents selected."""

    def main(self):
        """For all of the documents selected it will change the visibility of the notes
        on these documents to the one specified."""
        self.client.session.headers.update({'User-Agent': 'Change Note Visibility Add-On'})
        # fetch the access_level specified
        access_level = self.data["access_level"]
        accepted_values = ["private", "public", "organization"]
        if access_level not in accepted_values:
            self.set_message("You set an invalid access level. Try again.")
            sys.exit(1)
        for document in self.get_documents():
            for note in document.notes:
                note.access = access_level
                note.save()
            time.sleep(5)


if __name__ == "__main__":
    ChangeNoteVisibility().main()
