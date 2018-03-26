#!/usr/bin/env python3

import logging

from unittest import TextTestRunner

logger = logging.getLogger(__name__)


class ExampleTestRunner(TextTestRunner):

    def run(self, test):
        super(ExampleTestRunner, self).run(test)
