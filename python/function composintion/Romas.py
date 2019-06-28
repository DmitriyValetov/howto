from functools import reduce
from functools import partial

def f(*argv, **kwargs):
  print('f: {} {}'.format(argv, kwargs))
  return argv, kwargs

def g(*argv, **kwargs):
  print('g: {} {}'.format(argv, kwargs))
  return argv, kwargs

def compose(fs, *argv, **kwargs):
  return reduce(lambda x, y: y(*x[0], **x[1]), fs, (argv, kwargs))

h = partial(compose, [f, g])
h('value', key='value')

m = partial(compose, [h, f, g])
m('value', key='value')

compose([h, f, g], 'value', key='value')