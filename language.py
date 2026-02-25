"""
Language Management Component - DEPRECATED
This module now redirects to translation_service.py
Kept for backward compatibility with existing pages
"""

# Import everything from new translation service
from components.translation_service import (
    t,
    get_text,
    init_session_state,
    init_translation_state,
    load_custom_css,
    get_available_languages,
    get_current_language,
    render_language_selector,
    change_language,
    SUPPORTED_LANGUAGES,
    UI_TEXTS
)

# Re-export for backward compatibility
__all__ = [
    't',
    'get_text',
    'init_session_state',
    'init_translation_state',
    'load_custom_css',
    'get_available_languages',
    'get_current_language',
    'render_language_selector',
    'change_language',
    'SUPPORTED_LANGUAGES',
    'UI_TEXTS'
]
