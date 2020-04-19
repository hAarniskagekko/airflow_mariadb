#!/bin/bash

airflow initdb

airflow webserver -D

airflow scheduler -D
