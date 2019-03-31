# Change Log

## [**Next release**](https://galaxy.ansible.com/paulfantom/restic)

**Merged pull requests:**

- Delegate run\_once to localhost [\#55](https://github.com/paulfantom/ansible-restic/pull/55) ([TheLastProject](https://github.com/TheLastProject))

## [0.13.0](https://galaxy.ansible.com/paulfantom/restic) (2019-03-28)
**Closed issues:**

- "Deploy cron script" task treats “dest” as a directory instead of as a file and fails [\#46](https://github.com/paulfantom/ansible-restic/issues/46)

**Merged pull requests:**

- do not set binary capabilities when restic user is root [\#54](https://github.com/paulfantom/ansible-restic/pull/54) ([paulfantom](https://github.com/paulfantom))
- Propagate changes from cloudalchemy roles [\#52](https://github.com/paulfantom/ansible-restic/pull/52) ([paulfantom](https://github.com/paulfantom))
- Better handling of libcap2 installation [\#51](https://github.com/paulfantom/ansible-restic/pull/51) ([paulfantom](https://github.com/paulfantom))
- Add support for letting restic run certain commands with sudo [\#50](https://github.com/paulfantom/ansible-restic/pull/50) ([TheLastProject](https://github.com/TheLastProject))
- bump default restic version to 0.9.4 [\#49](https://github.com/paulfantom/ansible-restic/pull/49) ([kalos](https://github.com/kalos))
- more useful examples [\#48](https://github.com/paulfantom/ansible-restic/pull/48) ([kalos](https://github.com/kalos))
- Use restic helper instead raw restic command to initialize repositories [\#45](https://github.com/paulfantom/ansible-restic/pull/45) ([kalos](https://github.com/kalos))

## [0.12.1](https://galaxy.ansible.com/paulfantom/restic) (2018-12-28)
**Merged pull requests:**

- Don't try to chmod or chown files under /dev [\#43](https://github.com/paulfantom/ansible-restic/pull/43) ([madddi](https://github.com/madddi))
- bump default restic version to 0.9.3 [\#41](https://github.com/paulfantom/ansible-restic/pull/41) ([jkirk](https://github.com/jkirk))

## [0.12.0](https://galaxy.ansible.com/paulfantom/restic) (2018-12-18)
**Merged pull requests:**

- Fix cron and init [\#39](https://github.com/paulfantom/ansible-restic/pull/39) ([TheLastProject](https://github.com/TheLastProject))
- Allow controlling cron logging [\#38](https://github.com/paulfantom/ansible-restic/pull/38) ([TheLastProject](https://github.com/TheLastProject))

## [0.11.0](https://galaxy.ansible.com/paulfantom/restic) (2018-12-12)
**Merged pull requests:**

- Add helpers for easier backup restoring [\#37](https://github.com/paulfantom/ansible-restic/pull/37) ([TheLastProject](https://github.com/TheLastProject))
- Removed export from template [\#34](https://github.com/paulfantom/ansible-restic/pull/34) ([ntimo](https://github.com/ntimo))
- Add remote\_credentials to environment when initializing repositories [\#24](https://github.com/paulfantom/ansible-restic/pull/24) ([alo-is](https://github.com/alo-is))

## [0.10.0](https://galaxy.ansible.com/paulfantom/restic) (2018-12-05)
**Merged pull requests:**

- port CI changes from cloudalchemy repositories [\#36](https://github.com/paulfantom/ansible-restic/pull/36) ([paulfantom](https://github.com/paulfantom))
- Use comment filter for ansible\_managed. [\#35](https://github.com/paulfantom/ansible-restic/pull/35) ([SuperQ](https://github.com/SuperQ))
- bump version only [\#33](https://github.com/paulfantom/ansible-restic/pull/33) ([killua-eu](https://github.com/killua-eu))
- fiexd aws aws\_access\_key\_id var name [\#32](https://github.com/paulfantom/ansible-restic/pull/32) ([cryptozero](https://github.com/cryptozero))
- added export to restic vars [\#31](https://github.com/paulfantom/ansible-restic/pull/31) ([cryptozero](https://github.com/cryptozero))
- added architecture to temp restic executable file [\#30](https://github.com/paulfantom/ansible-restic/pull/30) ([cryptozero](https://github.com/cryptozero))
- fix for TASK \[paulfantom.restic : Get checksum for 386 architecture\] [\#29](https://github.com/paulfantom/ansible-restic/pull/29) ([cryptozero](https://github.com/cryptozero))
- bump default restic version to 0.9.2 [\#28](https://github.com/paulfantom/ansible-restic/pull/28) ([jkirk](https://github.com/jkirk))

## [0.9.0](https://galaxy.ansible.com/paulfantom/restic) (2018-08-19)
**Merged pull requests:**

- Bump default restic version to 0.9.2 [\#27](https://github.com/paulfantom/ansible-restic/pull/27) ([madddi](https://github.com/madddi))
- Create a home directory for the restic user [\#26](https://github.com/paulfantom/ansible-restic/pull/26) ([madddi](https://github.com/madddi))
- Optionally discard stdout of preconfigured cron jobs [\#25](https://github.com/paulfantom/ansible-restic/pull/25) ([madddi](https://github.com/madddi))
- Minor fixes for installation and custom user handling [\#23](https://github.com/paulfantom/ansible-restic/pull/23) ([hadret](https://github.com/hadret))
- be very explicit about client binary name [\#22](https://github.com/paulfantom/ansible-restic/pull/22) ([kaleng](https://github.com/kaleng))

## [0.8.0](https://galaxy.ansible.com/paulfantom/restic) (2018-05-15)
**Implemented enhancements:**

- allow specifying `latest` as version [\#19](https://github.com/paulfantom/ansible-restic/pull/19) ([paulfantom](https://github.com/paulfantom))
- Checksum verification [\#18](https://github.com/paulfantom/ansible-restic/pull/18) ([paulfantom](https://github.com/paulfantom))

**Merged pull requests:**

- Sanitize variables in jinja template [\#20](https://github.com/paulfantom/ansible-restic/pull/20) ([paulfantom](https://github.com/paulfantom))
- Repository initialization [\#10](https://github.com/paulfantom/ansible-restic/pull/10) ([paulfantom](https://github.com/paulfantom))

## [0.7.0](https://galaxy.ansible.com/paulfantom/restic) (2018-05-14)
**Implemented enhancements:**

- molecule 2.x tests and support for ubuntu bionic and debian stretch [\#17](https://github.com/paulfantom/ansible-restic/pull/17) ([paulfantom](https://github.com/paulfantom))

## [0.6.6](https://galaxy.ansible.com/paulfantom/restic) (2018-05-14)
**Merged pull requests:**

- make "restic check" execution configurable [\#16](https://github.com/paulfantom/ansible-restic/pull/16) ([kaleng](https://github.com/kaleng))
- only use remote\_credentials when needed [\#15](https://github.com/paulfantom/ansible-restic/pull/15) ([kaleng](https://github.com/kaleng))

## [0.6.5](https://galaxy.ansible.com/paulfantom/restic) (2018-02-07)
**Fixed bugs:**

- Restic installation directory chmod [\#12](https://github.com/paulfantom/ansible-restic/issues/12)

**Merged pull requests:**

- download restic to localhost in check mode [\#14](https://github.com/paulfantom/ansible-restic/pull/14) ([kaleng](https://github.com/kaleng))

## [0.6.4](https://galaxy.ansible.com/paulfantom/restic) (2018-02-02)
**Merged pull requests:**

- Don't set file permission for installation dir [\#13](https://github.com/paulfantom/ansible-restic/pull/13) ([paulfantom](https://github.com/paulfantom))

## [0.6.3](https://galaxy.ansible.com/paulfantom/restic) (2018-01-08)
## [0.6.2](https://galaxy.ansible.com/paulfantom/restic) (2018-01-08)
**Merged pull requests:**

- merge upstream [\#11](https://github.com/paulfantom/ansible-restic/pull/11) ([paulfantom](https://github.com/paulfantom))
- secure user-based installation [\#9](https://github.com/paulfantom/ansible-restic/pull/9) ([paulfantom](https://github.com/paulfantom))

## [0.6.1](https://galaxy.ansible.com/paulfantom/restic) (2018-01-06)
**Merged pull requests:**

- merge upstream [\#8](https://github.com/paulfantom/ansible-restic/pull/8) ([paulfantom](https://github.com/paulfantom))
- Cleanup [\#7](https://github.com/paulfantom/ansible-restic/pull/7) ([paulfantom](https://github.com/paulfantom))

## [0.6.0](https://galaxy.ansible.com/paulfantom/restic) (2018-01-06)
**Merged pull requests:**

- Remove password files [\#6](https://github.com/paulfantom/ansible-restic/pull/6) ([paulfantom](https://github.com/paulfantom))

## [0.5.2](https://galaxy.ansible.com/paulfantom/restic) (2018-01-05)
**Merged pull requests:**

- apply repository checking and retention policies [\#5](https://github.com/paulfantom/ansible-restic/pull/5) ([paulfantom](https://github.com/paulfantom))

## [0.5.1](https://galaxy.ansible.com/paulfantom/restic) (2018-01-05)
**Merged pull requests:**

- fix directory creation [\#4](https://github.com/paulfantom/ansible-restic/pull/4) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.5.0](https://galaxy.ansible.com/paulfantom/restic) (2018-01-04)
**Merged pull requests:**

- Major rework [\#3](https://github.com/paulfantom/ansible-restic/pull/3) ([paulfantom](https://github.com/paulfantom))
- download and propagate [\#2](https://github.com/paulfantom/ansible-restic/pull/2) ([paulfantom](https://github.com/paulfantom))
- add support for more backends [\#1](https://github.com/paulfantom/ansible-restic/pull/1) ([paulfantom](https://github.com/paulfantom))

## [0.4](https://galaxy.ansible.com/paulfantom/restic) (2017-12-13)
## [0.3](https://galaxy.ansible.com/paulfantom/restic) (2017-12-13)
## [0.2](https://galaxy.ansible.com/paulfantom/restic) (2017-12-05)
## [0.1](https://galaxy.ansible.com/paulfantom/restic) (2017-12-05)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*