import pytest

def admin_command(command, sudo=True):
    if not isinstance(command, list):
        raise TypeError(f"Era esperado que o comando fosse uma lista, mas é do tipo: {type(command)}")
    if sudo:
        return ["sudo"] + command
    return command

class TestAdminCommand: 
    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected

    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("Algum comando", sudo=True)
        assert error.value.args[0] == "Era esperado que o comando fosse uma lista, mas é do tipo <class 'str'>"