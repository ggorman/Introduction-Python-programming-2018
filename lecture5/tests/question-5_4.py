test = {
  'name': 'question 5.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(y(1, 1), -3.9050000000000002)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sanity_check(y, -1, -1)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
def sanity_check(fxn, arg1, arg2):
    try:
        y(-1, -1)
        return False
    except:
        return True
    return False
    """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
