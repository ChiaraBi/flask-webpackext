# -*- coding: utf-8 -*-
#
# This file is part of Flask-WebpackExt
# Copyright (C) 2018 CERN.
#
# Flask-WebpackExt is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Webpack bundle APIs for Flask-WebpackExt."""

from __future__ import absolute_import, print_function

from pywebpack import WebpackBundle as PyWebpackBundle


class WebpackBundle(PyWebpackBundle):
    """Flask webpack bundle."""

    def __init__(self, import_name, folder, **kwargs):
        """Initialize bundle.

        :param import_name: Name of the module where the WebpackBundle class
            is instantiated. It is used to determine the absolute path to the
            ``folder`` where the assets are located.
        :param folder: Relative path to the assets.
        :param kwargs: Keyword arguments directly passed to
            :class:`pywebpack.bundle.WebpackBundle`.
        """
        super(WebpackBundle, self).__init__(
            join(get_root_path(import_name), folder),
            **kwargs
        )
