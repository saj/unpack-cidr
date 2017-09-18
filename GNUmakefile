DIST_DIR      := $(CURDIR)/dist
BUILD_DIR     := $(CURDIR)/build
PEX_CACHE_DIR := $(BUILD_DIR)/pex/cache

NAME := $(shell python setup.py --name)

# https://github.com/tox-dev/tox/issues/412
.NOTPARALLEL:


.PHONY: all
all:
	$(MAKE) lint
	$(MAKE) test
	$(MAKE) dist


.PHONY: clean
clean:
	rm -fr '$(DIST_DIR)'
	rm -fr '$(BUILD_DIR)'


.PHONY: lint
lint:
	$(MAKE) lint-py27
	$(MAKE) lint-py34


.PHONY: test
test:
	$(MAKE) test-py27
	$(MAKE) test-py34


.PHONY: dist
dist:
	$(MAKE) dist-pex-py27
	$(MAKE) dist-pex-py34


.PHONY: lint-py27
lint-py27: _version.py
	tox --workdir "$(BUILD_DIR)/tox" -e lint-py27


.PHONY: lint-py34
lint-py34: _version.py
	tox --workdir "$(BUILD_DIR)/tox" -e lint-py34


.PHONY: test-py27
test-py27:
	tox --workdir "$(BUILD_DIR)/tox" -e nose-py27


.PHONY: test-py34
test-py34:
	tox --workdir "$(BUILD_DIR)/tox" -e nose-py34


.PHONY: dist-pex-py27
dist-pex-py27: $(PEX_CACHE_DIR) $(DIST_DIR) _version.py
	find '$(PEX_CACHE_DIR)' -name "$$(echo $(NAME) | sed 's/-/_/g')-*.whl" -delete
	env \
		DIST_DIR='$(DIST_DIR)' \
		PEX_CACHE_DIR='$(PEX_CACHE_DIR)' \
		tox --workdir "$(BUILD_DIR)/tox" -e dist-pex-py27


.PHONY: dist-pex-py34
dist-pex-py34: $(PEX_CACHE_DIR) $(DIST_DIR) _version.py
	find '$(PEX_CACHE_DIR)' -name "$$(echo $(NAME) | sed 's/-/_/g')-*.whl" -delete
	env \
		DIST_DIR='$(DIST_DIR)' \
		PEX_CACHE_DIR='$(PEX_CACHE_DIR)' \
		tox --workdir "$(BUILD_DIR)/tox" -e dist-pex-py34


$(DIST_DIR):
	mkdir -p '$@'


$(PEX_CACHE_DIR):
	mkdir -p '$@'


.PHONY: _version.py
_version.py:
	scripts/mkversion '$@'
