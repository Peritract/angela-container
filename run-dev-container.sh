docker run -it --mount type=bind,src="$(pwd)"/code,dst=/code --workdir=/code python:latest bash