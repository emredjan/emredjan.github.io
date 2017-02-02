Details on installing and usage on Windows Bash:

[Dave Rupert - Ruby on Rails on Bash on Ubuntu on Windows](http://daverupert.com/2016/06/ruby-on-rails-on-bash-on-ubuntu-on-windows/)  
[Richard Banks - Jekyll on Bash on Ubuntu on Windows](https://www.richard-banks.org/2016/08/jekyll-on-bash-on-ubuntu-on-windows.html)  
[Dave Rupert - Jekyll on Windows with Bash](http://daverupert.com/2016/04/jekyll-on-windows-with-bash/)  
<br/>
Themes  
[Pixyll](https://github.com/johnotander/pixyll)  
<br/>
Code to execute on windows bash
```bash
bundle exec jekyll serve --force_polling --incremental
```
<br/>
Details on installing and usage on macOS:

[Jekyll Installation Pages](https://jekyllrb.com/docs/installation/)  
[RubyGems Installation Pages](https://rubygems.org/pages/download)

```bash
# install ruby
brew install ruby

# install rubygems from above & update
gem update --system
# or update with this if above doesn't work
gem install rubygems-update
update_rubygems

# install bundler and bundleß
gem install bundler
sudo bundle install
```
<br/>
<br/>
Code to execute on macOS

```bash
bundle exec jekyll serve --watch
```
