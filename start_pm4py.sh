# Mounts current dir to pm4py dir in container
docker run -v"`pwd`":/pm4py -it javert899/pm4py:latest bash
