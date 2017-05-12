---
layout:     post
title:      Upgrade bash in Windows 10
date:       2017-04-06 20:20:00
summary:    Easily upgrade the bash shell in Windows 10 Creators Update without reinstalling
categories: blog
tags:       windows bash WSL
published:  true
---

One of the not-much-advertised featues of the new [Creators update for Windows 10](https://www.microsoft.com/en-us/windows/upcoming-features) is the support for Ubuntu 16.04 in Windows Subsytem for Linux (WSL). The catch is, if you installed the WSL prior to upgrading Windows, it will not upgrade it for you, and leave it as Ubuntu 14.04.

If you want the latest LTS Ubuntu, one option is delete the WSL and reinstall using (in powershell):

{% highlight shell %}

lxrun /uninstall
lxrun /install

{% endhighlight %}

This, however will delete all your linux settings / files under WSL, which may be an inconvenience. A less destructive option is to just use (in bash):

{% highlight shell %}

sudo do-release-upgrade

{% endhighlight %}

Which works *surprisingly* well, and doesn't take too long to complete on a modern system. See for yourself:

##### Before upgrade:

<img src="{{ site.baseurl }}/images/ubuntu_before.png">

##### Upgrading:

<img src="{{ site.baseurl }}/images/ubuntu_during.png">

##### After upgrade:

<img src="{{ site.baseurl }}/images/ubuntu_after.png">


<br><br>
**Bonus:** `libinotify` now works and so does `jekyll --watch` ([more info](https://github.com/Microsoft/BashOnWindows/issues/216))

<img src="{{ site.baseurl }}/images/jekyll_regenerate.png">
