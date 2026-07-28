import os


class ResumeScreener:

    @staticmethod
    def get_resumes(folder):

        resumes = []

        for file in os.listdir(folder):

            if file.lower().endswith((".pdf", ".docx")):

                resumes.append(
                    os.path.join(folder, file)
                )

        return resumes