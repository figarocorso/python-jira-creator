## python-jira-creator

This repo has two scripts:

* One for creating a Jira task with some handy defaults so you only have to enter summary and description.
* One for opening a given issue in your browser (just because we hear to often in meetings FOO-XYZ and we wanna open that fast)


### Configuring defaults

Before launching the script you probably want to edit `config.json` so it looks like:

```
{
    "defaults": {
        "component": "Component",
        "epic": "FOO-173",
        "project": "FOO"
    },
    "credentials": {
        "username": "me@company.org",
        "password": "token",
        "server": "https://company.atlassian.net"
    }
}
```

### Launching any of them

We can use virtualenv to avoid installing deps, but easiest way:

```
pip install -r requirements.txt
python pjc.py
```

Or maybe:

```
python pjo.py FOO-123
# or just python pjo.py
```

### Contributing

This is some nasty ugly shit. Consider opening any issue with your ideas (but it would be better if you open a PR). If we keep script interaction hacker fast, PRs would be also merged fast. Styling, testing, terminal colors, libraries, ... everything is welcome.
