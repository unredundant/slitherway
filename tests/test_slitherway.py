from testcontainers.postgres import PostgresContainer

from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs


def test_run_migrations():
    with PostgresContainer("postgres:14") as pg:
        args = FlywayCommandArgs(
            user=pg.POSTGRES_USER,
            password=pg.POSTGRES_PASSWORD,
            locations=["migrations"],
            url=f"jdbc:postgresql://localhost:{pg.get_exposed_port(5432)}/{pg.POSTGRES_DB}",
        )

        result = migrate(args)
        assert result.returncode == 0
