#!/bin/bash

yw_jar=~/bin/yesworkflow-0.2.1.1-jar-with-dependencies.jar

java -jar $yw_jar graph
dot -Tpng ./outputs/Overall_Workflow.gv -o ./outputs/Overall_Workflow.png