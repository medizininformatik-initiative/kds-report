# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),


## [2.1.0] - 2026-05-06

### Added

- Added Encounter queries - distinguish between full and part inpatient, add class and status finished
- Added Consent query which considers: category, status and type and fix to .8 provision ([#41](https://github.com/medizininformatik-initiative/kds-report/issues/41))

### Changed

- Make search bundle version configurable
- Add two extra years from date of generation to year queries ([#42](https://github.com/medizininformatik-initiative/kds-report/issues/42))
- Update search bundle identifier to new naming system ([#37](https://github.com/medizininformatik-initiative/kds-report/issues/37))

## [2.0.3] - 2025-02-03

### Added

- Added new queries for new modules ([#27](https://github.com/medizininformatik-initiative/kds-report/issues/27))


## [2.0.2] - 2024-11-27

### Fixed

- Fixed typo in ObservationLab query  ([#25](https://github.com/medizininformatik-initiative/kds-report/issues/25))


## [2.0.1] - 2024-08-07

### Changed

- Changed Ecnounter year queries to only count `einrichtungskontakt`  ([#20](https://github.com/medizininformatik-initiative/kds-report/issues/20))


## [2.0.0] - 2024-06-10

### Added

- Added "category" field to queries ([#9](https://github.com/medizininformatik-initiative/kds-report/issues/9))
- Changed queries to use :below modifier ([#10](https://github.com/medizininformatik-initiative/kds-report/issues/10))


## [1.1.0] - 2024-06-10

### Added

- Added system queries ([#6](https://github.com/medizininformatik-initiative/kds-report/issues/6))
- Updated search bundle version

## [1.0.0] - 2023-11-12

- Initialized project

### Added

- Add basic report queries to count number of resources available for each profile
- Yearly Query for encounter
- Added validator
- Added dsf search bundle generator
- Added report schema
