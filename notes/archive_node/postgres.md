# Working with Postgres

## Install from source

### Install dependencies

Before building PostgreSQL from source, you will need to install some dependencies. You can do this with the following command:

```sh
sudo apt-get install build-essential libreadline-dev zlib1g-dev flex bison libxml2-dev libxslt-dev libssl-dev
```

### Download source

Download the [source code](https://www.postgresql.org/ftp/source/) from the PostgreSQL website. Once you have the file, extract it with the following command:

```sh
tar xvfz postgresql-VERSION.tar.gz
```

### Configure and build

Once the source code is extracted, you can configure and build it with the following commands:

```sh
cd postgresql-VERSION
./configure
make
```

### Install

Once the build is complete, you can install PostgreSQL with the following command:

```sh
sudo make install
```

### Add `postgres` user and add env vars

Add user and set password

```sh
adduser postgres
sudo passwd postgres
```

Switch to `postgres` user and add env vars

```sh
su - postgres
nano ~/.bashrc
```

Add the following to `~/.bashrc`

```sh
LD_LIBRARY_PATH=/usr/local/pgsql/lib
export LD_LIBRARY_PATH

PATH=/usr/local/pgsql/bin:$PATH
export PATH

MANPATH=/usr/local/pgsql/share/man:$MANPATH
export MANPATH
```

Save `~/.bashrc` and refresh `source ~/.bashrc`

### Initialize the db

Once PostgreSQL is installed, you can initialize the database with the following command:

```sh
initdb -D /usr/local/pgsql/data
```

You can now start the PostgreSQL server

(make sure no other postgres instances are running, see [postgres](./../helpful_commands.md#postgresql))

```sh
postgres -D /usr/local/pgsql/data >logfile 2>&1 &
```

(if env vars have not been set in `~/.bashrc`, then use fully qualified command `/usr/local/pgsql/bin/COMMAND`)

Follow [instructions](https://www.postgresql.org/docs/current/installation.html) to build from source

### Config loc

`postgresql.conf` is located in `/etc/postgresql/VERSION/main/`
