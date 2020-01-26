import cv2

from .base import BaseTestCase, root


try:
    cv2.setNumThreads(1)
except AttributeError:
    print('!!! You are using OpenCV which does not allow you to set '
          'the number of threads')


class Cv2TestCase(BaseTestCase):
    filter_ids = {
        cv2.INTER_AREA: 'sup',
        cv2.INTER_NEAREST: 'ner',
        cv2.INTER_LINEAR: 'bil',
        cv2.INTER_CUBIC: 'bic',
        cv2.INTER_LANCZOS4: 'lzs4',
    }

    def create_test_data(self):
        im = cv2.imread(root('resources', 'color_circle.png'),
                        flags=cv2.IMREAD_UNCHANGED)
        if self.mode == 'RGB':
            im = im[:, :, :3]
        elif self.mode == 'RGBA':
            pass
        elif self.mode == 'L':
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        else:
            raise ValueError('Unknown mode: {}'.format(self.mode))

        # Fine for upscaling
        im = cv2.resize(im, tuple(self.size), interpolation=cv2.INTER_CUBIC)
        return [im]
