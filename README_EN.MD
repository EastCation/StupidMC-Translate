# StupidMC Translate

## MoeRain Codeopen Project

## Introduction

This is the work of Starmoe and MoeRain Software Developments - StupidMC Translate. This translation pack has the same power as APT.

## File structure

The current version of the sandsculpture translation package file structure is shown below. (* indicates that it can be deleted after downloading, without affecting use)

```Python

<ROOT>
    <pack.mcmeta># Resource pack metafile, deletion will make the resource pack unavailable
    [assets]
    [bedrockify]# Bedrockif-compatible modules
        [lang]
            <zh_cn.json>
    [minecraft]# Original Minecraft compatible modules
        [lang]# Language file
            *<en_us.json># English original language file (may be outdated)
            <zh_cn.json># Sand sculpture translation package core - Chinese language file
            *<zh_cn-233.json># Old community language file, not fully translated
        [texts]# Generic text files (e.g. ending poems and credits)
            <credits.json># Current credits
            <Credits.txt ># Old credits created for backward compatibility (stopped updating)
            <end.txt># end poem original and translation
            <end.txt.bak># A copy of the above file
            <postcredits.txt># The final poem and the message after the credits
            <splashs.js ># backward compatible flashing tagline (stop updating)
            <splashs.txt ># Main screen flashing yellow sand-carved text (flashing slogan)

```

## Usage

### Modrinth version Download (recommended)

If your launcher comes with the ability to retrieve resource packs from Modrinth, you can simply search for "Stupid MC" and then follow the launcher instructions to install it.

If you are not with the starter of resource bundles from Modrinth retrieval function, you can use [this link](https://modrinth.com/resourcepack/stupid-mc-translate-chn) to download, Modrinth zip need not stress. You can use it directly in the Resource pack folder.

### git version download

In here to download [Release](https://github.com/EastCation/StupidMC-Translate/releases), After you get the package, put <StupidMC-Translate- version> in your version of the [resourcespacks] folder, and then in the Minecraft resource pack selection screen should be visible, loading at the top can be used (this package has no texture change function, please feel free to use).

## React with other resource packs

This resource pack can be used in combination with the Chinese resource pack. However, before using, please make sure that *Compatibility mode* is enabled on your Block Chinese resource pack and that this resource pack is at the top, otherwise you will only see the block Chinese translation.

This resource pack is recommended [StupidMC Addon Pack](https://starmoe-my.sharepoint.com/:f:/g/personal/starmoe_starmoe_com_mp/EvBq1wLCheJPiRnwIoZheEoB0HmMHYtBppgRUlmbveV69A?e=tElcnX)to use, otherwise it may be a lot less fun.

## How to contribute

You need to Fork or Git the repository, then create your masterpiece locally, and if you think you're done, submit your PR

If there is a conflict in PR, we will first follow the principle of "first come, first served", if the latter has a better translation than the former, we will consider the latter over the former.

If you have any questions about this resource pack, please open an issue to discuss it with us.

If it is a matter of personal privacy, you can also send an email to [starmoe@starmoe.com.mp](mailto:starmoe@starmoe.com.mp) and we will do our best to resolve it.

## Open source license

This translation package is licensed under the [GNU GPLv3](LICENSE) license terms.
