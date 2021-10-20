docs:
	docker run \
	--rm \
	-e ANSIBLE_DOCTOR_ROLE_NAME=bitwarden \
	-e ANSIBLE_DOCTOR_ROLE_DIR=/doctor/ \
	-e ANSIBLE_DOCTOR_OUTPUT_DIR=/doctor/ \
	-e ANSIBLE_DOCTOR_FORCE_OVERWRITE=true \
	-e ANSIBLE_DOCTOR_LOG_LEVEL=info \
	-e ANSIBLE_DOCTOR_CUSTOM_HEADER=HEADER.md \
	-e PY_COLORS=1 \
	-v $$(pwd):/doctor \
	-w /doctor \
	thegeeklab/ansible-doctor