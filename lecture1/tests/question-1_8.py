test = {
  'name': 'question 1.8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose( perfect_egg(4), 326.2798626986453)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose( perfect_egg(20), 259.342856)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
