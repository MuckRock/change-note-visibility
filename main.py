"""
This is an Add-On that allows you to change the visibility of all notes queried or selected.
"""

from documentcloud.addon import AddOn, SoftTimeOutAddOn

class ChangeNoteVisibility(SoftTimeOutAddOn):
    """Bulk changes visibility of notes on documents selected."""

    def main(self):
        """For all of the documents selected it will change the visibility of the notes 
           on these documents to the one specified."""
        # fetch the access_level specified
        access_level = self.data["access_level"]
        accepted_values = ['private', 'public', 'organization']
        if access_level not in accepted_values:
            self.set_message("You set an invalid access level- must be private, public, or organization")
            sys.exit(1)
        for document in self.get_documents():
            for note in document.notes:
                note.access = access_level
                note.save()

if __name__ == "__main__":
    ChangeNoteVisibility().main()
