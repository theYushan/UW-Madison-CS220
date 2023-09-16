{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c4ab777",
   "metadata": {
    "deletable": false,
    "editable": false
   },
   "outputs": [],
   "source": [
    "# Initialize Otter\n",
    "import otter\n",
    "grader = otter.Notebook(\"p1.ipynb\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e74d2417",
   "metadata": {},
   "outputs": [],
   "source": [
    "# PLEASE FILL IN THE DETAILS\n",
    "# Enter None if you don't have a project partner\n",
    "\n",
    "# project: p1\n",
    "# submitter: NETID1\n",
    "# partner: NETID2\n",
    "# hours: ????"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e26ac162",
   "metadata": {},
   "source": [
    "**Question 1:** \"Hello, World!\" program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6338f568",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "name = \"World\"\n",
    "greeting = \"Hello, \" + name + \"!\"\n",
    "greeting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f91c60dc",
   "metadata": {
    "deletable": false,
    "editable": false
   },
   "outputs": [],
   "source": [
    "grader.check(\"q1\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a7395bc",
   "metadata": {},
   "source": [
    "**Question 2:** Compute current year."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ad71933",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "curr_year = 45 * 45 - 3\n",
    "curr_year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddd91fef",
   "metadata": {
    "deletable": false,
    "editable": false
   },
   "outputs": [],
   "source": [
    "grader.check(\"q2\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e011d98",
   "metadata": {
    "deletable": false,
    "editable": false
   },
   "source": [
    "## Submission\n",
    "\n",
    "Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**\n",
    "\n",
    "SUBMISSION INSTRUCTIONS: The zipfile automatically gets downloaded. You should have received GradeScope invite - please accept it. Login to GradeScope and upload the zipfile. Check otter results as soon as auto-grader gets completed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df396ce3",
   "metadata": {
    "deletable": false,
    "editable": false
   },
   "outputs": [],
   "source": [
    "# Save your notebook first, then run this cell to export your submission.\n",
    "grader.export(pdf=False, run_tests=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6aa13ea6",
   "metadata": {},
   "source": [
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "otter": {
   "OK_FORMAT": true,
   "tests": {
    "q1": {
     "name": "q1",
     "points": 12.5,
     "suites": [
      {
       "cases": [
        {
         "code": ">>> greeting == \"Hello, World!\"\nTrue",
         "hidden": false,
         "locked": false
        }
       ],
       "scored": true,
       "setup": "",
       "teardown": "",
       "type": "doctest"
      }
     ]
    },
    "q2": {
     "name": "q2",
     "points": 12.5,
     "suites": [
      {
       "cases": [
        {
         "code": ">>> curr_year == 2022\nTrue",
         "hidden": false,
         "locked": false
        }
       ],
       "scored": true,
       "setup": "",
       "teardown": "",
       "type": "doctest"
      }
     ]
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
