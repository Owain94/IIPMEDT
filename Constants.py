class Constants(object):
    def __init__(self, *args, **kwargs) -> None:
        self._d = dict(*args, **kwargs)

    def __iter__(self) -> iter:
        return iter(self._d)

    def __len__(self) -> int:
        return len(self._d)

    def __getattr__(self, name: any) -> any:
        return self._d[name]

    def __setattr__(self, name: str, value: any) -> None:
        if name[0] == '_':
            super(Constants, self).__setattr__(name, value)
        else:
            raise ValueError("setattr while locked", self)
