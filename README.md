# scrcpy-fedora

Some experiments with the SPEC file to create an RPM for fedora.

The source of *scrcpy* is here: [scrcpy](https://github.com/Genymobile/scrcpy)

The current build requires internet access and the additional repo [RPMFusion-Free](https://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/)

#### Might be worth checking out too ...

The files *getsources.sh* and *.github/workflows/rpmbuild_copr.yml* are used for automated RPM package builds using [Github Actions](https://github.com/useidel/scrcpy-fedora/actions) and [Copr](https://copr.fedorainfracloud.org/coprs/useidel/scrcpy/).

