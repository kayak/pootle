# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from contextlib import contextmanager

import pytest

from pootle.core.contextmanagers import keep_data
from pootle.core.delegate import wordcount


@contextmanager
def _no_wordcount():
    from pootle_store.models import Unit

    with keep_data(signals=(wordcount, ), suppress=(Unit, )):
        yield


@pytest.fixture
def no_wordcount():
    return _no_wordcount
