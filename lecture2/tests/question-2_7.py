test = {
  'name': 'question 2.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(distances_list)==list
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'distances_list=distance(0.1, 0.6, 6)',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(distance(0.1, 0.6, 6), [0.5019, 0.8076000000000001, 0.9171, 0.8304, 0.5474999999999999, 0.06839999999999957])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(distance(1, 6, 5, 3),[-6.8100000000000005, -8.570100000000002, -10.5264, -12.6789, -15.0276])
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
