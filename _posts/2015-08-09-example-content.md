---
title: Example content
---

<p class="lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ullamcorper est in imperdiet molestie. Curabitur aliquet sem in ante venenatis.</p>

Morbi ultrices libero imperdiet [lectus](#) dignissim, sit amet bibendum nisl consectetur. Morbi erat purus, pretium at ligula tincidunt, faucibus commodo sem. Etiam vel porttitor est, vitae maximus ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sapien turpis, cursus non porta ac.

## Lorem
Quisque sodales euismod nibh, gravida venenatis nibh dignissim eget. Morbi gravida enim vel lectus aliquet aliquet.

### Ipsum
Nunc nec aliquam tellus. Etiam faucibus magna nibh, ut fermentum velit consectetur id. Nullam vehicula iaculis tortor, in cursus enim auctor vitae. Duis semper pulvinar justo, at vestibulum dolor. Cras fermentum nibh quis nisl imperdiet ornare. Sed nisi nunc, dictum sit amet gravida in, finibus rhoncus orci. Donec scelerisque commodo turpis ac venenatis.

> Nam vitae commodo ex. Nunc vel tellus leo.

## Dugem
Nullam vehicula iaculis tortor, in cursus enim auctor vitae. Duis semper pulvinar justo, at vestibulum dolor. Cras fermentum nibh quis nisl imperdiet ornare. Sed nisi nunc, dictum sit amet gravida in, finibus rhoncus orci. Donec scelerisque commodo turpis ac venenatis.

{% highlight py %}

# this script is used on windows to wrap shortcuts so that they are executed within an environment
#   It only sets the appropriate prefix PATH entries - it does not actually activate environments

import os
import sys
import subprocess
from os.path import join

from menuinst.knownfolders import FOLDERID, get_folder_path, PathNotFoundException

# call as: python cwp.py PREFIX ARGs...

prefix = sys.argv[1]
args = sys.argv[2:]

env = os.environ.copy()
env['PATH'] = os.path.pathsep.join([
        prefix,
        join(prefix, "Scripts"),
        join(prefix, "Library", "bin"),
        env['PATH'],
])

try:
    #documents_folder = get_folder_path(FOLDERID.Documents)
    documents_folder = "D:\\GoogleDrive\\Development\\"
except PathNotFoundException:
    documents_folder = get_folder_path(FOLDERID.PublicDocuments)
os.chdir(documents_folder)
subprocess.call(args, env=env)

{% endhighlight %}

{% highlight r %}

# Read in the data
stevens = read.csv("stevens.csv")
str(stevens)

# Split the data
library(caTools)
set.seed(3000)
spl = sample.split(stevens$Reverse, SplitRatio = 0.7)
Train = subset(stevens, spl==TRUE)
Test = subset(stevens, spl==FALSE)

# Install rpart library

library(rpart)

library(rpart.plot)

# CART model
StevensTree = rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, method="class", minbucket=25)

prp(StevensTree)

{% endhighlight %}



### Golem
Quisque sodales euismod nibh, gravida venenatis nibh dignissim eget. Morbi gravida enim vel lectus aliquet aliquet.

* Praesent commodo cursus magna.
* Donec id elit non mi porta gravida at eget metus.
* Nulla vitae elit libero, a pharetra augue.

Cras fermentum nibh quis nisl imperdiet ornare. Sed nisi nunc, dictum sit amet gravida in, finibus rhoncus orci. Donec scelerisque commodo turpis ac venenatis.

1. Vestibulum id ligula porta felis euismod semper.
2. Cum sociis natoque penatibus.
3. Maecenas sed diam eget risus.

Nam ante lacus, ornare ut lacus in, aliquet gravida orci. Donec non dignissim elit. Integer facilisis lorem sed porttitor elementum. Etiam a eleifend justo. 

<dl>
  <dt>HyperText Markup Language (HTML)</dt>
  <dd>The language used to describe and define the content of a Web page</dd>

  <dt>Cascading Style Sheets (CSS)</dt>
  <dd>Used to describe the appearance of Web content</dd>

  <dt>JavaScript (JS)</dt>
  <dd>The programming language used to build advanced Web sites and applications</dd>
</dl>

Sed nisi nunc, dictum sit amet gravida in, finibus rhoncus orci. Donec scelerisque commodo turpis ac venenatis.

![Large example image](http://placehold.it/800x400 "Large example image")
![Medium example image](http://placehold.it/400x200 "Medium example image")
![Small example image](http://placehold.it/200x200 "Small example image")

Aenean lacinia bibendum nulla sed consectetur. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Rank</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cookie</td>
      <td>#69</td>
      <td>169</td>
    </tr>
    <tr>
      <td>Buther</td>
      <td>#70</td>
      <td>169</td>
    </tr>
    <tr>
      <td>Stuart</td>
      <td>#71</td>
      <td>168</td>
    </tr>
  </tbody>
</table>

Nullam quis risus eget urna mollis ornare vel eu leo.
