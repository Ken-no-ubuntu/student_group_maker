# Group Maker GUI — Description

This Python script creates a simple graphical user interface (GUI) to randomly divide students into groups, considering absences.

## Features

* Uses **Tkinter** to provide an easy-to-use GUI.
* Supports specifying the **number of groups** to create.
* Allows marking **absent students** from a checklist so they are excluded.
* Randomly distributes present students from two grade levels (3rd and 4th year) evenly across groups.
* Displays the grouped students in a scrollable text box.

![screenshot](https://github.com/Ken-no-ubuntu/student_group_maker/blob/main/assets/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-07-04%20150828.png)

## Student Data

* **4th Year Students:** A fixed list of 6 names.
* **3rd Year Students:** A fixed list of 9 names.
* Students marked absent will be excluded from grouping.

## How It Works

1. User inputs the desired number of groups.
2. User selects absent students by checking their names.
3. On clicking "Generate Groups," the app:

   * Filters out absent students.
   * Shuffles and distributes the remaining 3rd and 4th year students evenly across the specified groups.
4. Groups and their members are displayed in the output box.

![screenshot](https://github.com/Ken-no-ubuntu/student_group_maker/blob/main/assets/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-07-04%20150843.png)

## Requirements

* Python 3.x
* Tkinter library (usually included with Python)

## How to Run

Run the script directly with Python:

```bash
python your_script_name.py
```
