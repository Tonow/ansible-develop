#!/usr/bin/env python3
import sys
import os
import tempfile
from subprocess import call, check_call
EDITOR = os.environ.get('EDITOR','vim')

class InstallTools:
    """Object to automate process with Jira.
    """

    def __init__(self, **kwarg):
        """Jira and github must be retrieved before in the authentication part.
        """
        # Input arg
        self.script_path = kwarg.get('script_path')

    def choose_task(self):
        """
            Retrive tasks in file and return a list
        """
        tasks = 'Any tasks find'
        with open(self.script_path) as script:
            for line in script:
                if line.startswith('# task: '):
                    tasks = line[8:-1]
                    return tasks.split(', ')
        return tasks

    def _check_task_list(self, tasks):
        """ Edit interactively the list of tasks.
            Like that we are able to remove tasks and add some tasks

            :param tasks: task list
            :return: task list updated by the user

            # TODO: Maybe also output the ignored lines.
        """
        initial_message = '\n'.join(tasks)
        initial_message = "# Install list :\n" + \
            initial_message + \
            "\n# Remove some of them if you want"

        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message.encode('ascii'))
            tf.flush()
            call([EDITOR, tf.name])

            # do the parsing with `tf` using regular File operations.
            # for instance:
            tf.seek(0)
            edited_message = tf.read()
        # Decode and remove the comment
        tasks_updated = edited_message.decode(
            'ascii'
        ).split('\n')[1:-2]
        tasks_updated_formated = self._add_quote(tasks_updated)
        return tasks_updated_formated

    def _add_quote(self, tasks_updated):
        for task in tasks_updated:
            task = "'" + str(task) + "'"
        return tasks_updated

    def run_bash_script(self, tasks):
        script_call = ["./" + self.script_path] + tasks
        print(script_call)
        call(script_call, shell=True)


def main(script_path):
    """
        Helper to manage install scripts
    """

    kwargs = {
        'script_path': script_path,
    }
    tools = InstallTools(**kwargs)
    tasks = tools.choose_task()
    tasks_updated = tools._check_task_list(tasks)
    tools.run_bash_script(tasks_updated)

if __name__ == "__main__":
    main('cmd_install')
