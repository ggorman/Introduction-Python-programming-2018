test = {
  'name': 'question 1.9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose( period(1.5*10**11), [58059817.3950661, 31603718.929927427])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose( birthdays, 18.37119787)
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
