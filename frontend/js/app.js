// Tamil Story Generator - App Logic with Translation

class StoryApp {
    constructor() {
        this.selectedKeyword = null;
        this.currentStory = null;
        this.languages = {
            'en': 'English',
            'ta': 'தமிழ்',
            'hi': 'हिंदी',
            'te': 'తెలుగు',
            'ml': 'മലയാളം',
            'kn': 'ಕನ್ನಡ',
            'ur': 'اردو'
        };
        this.init();
    }

    init() {
        document.querySelectorAll('.kw').forEach(kw => {
            kw.addEventListener('click', () => this.select(kw));
        });
        document.getElementById('generateBtn').addEventListener('click', () => this.generate());
        document.getElementById('clearBtn').addEventListener('click', () => this.clear());
        this.updateUI();
    }

    select(el) {
        const keyword = el.dataset.keyword;
        if (el.classList.contains('selected')) {
            this.selectedKeyword = null;
            el.classList.remove('selected');
        } else {
            document.querySelectorAll('.kw.selected').forEach(k => k.classList.remove('selected'));
            this.selectedKeyword = keyword;
            el.classList.add('selected');
        }
        this.updateUI();
    }

    updateUI() {
        const hasSelection = this.selectedKeyword !== null;
        document.getElementById('keywordCount').textContent = hasSelection ? '1' : '0';
        document.getElementById('progressFill').style.width = hasSelection ? '100%' : '0%';
        
        const tags = document.getElementById('selectedTags');
        if (!hasSelection) {
            tags.innerHTML = '<span class="placeholder">Click any keyword below to select</span>';
        } else {
            tags.innerHTML = `<span class="sel-tag">${this.selectedKeyword} <span class="x">×</span></span>`;
            tags.querySelector('.sel-tag').addEventListener('click', () => this.clear());
        }
        document.getElementById('generateBtn').disabled = !hasSelection;
    }

    clear() {
        this.selectedKeyword = null;
        document.querySelectorAll('.kw.selected').forEach(kw => kw.classList.remove('selected'));
        this.updateUI();
    }

    getAge() {
        return document.querySelector('input[name="age"]:checked')?.value || 'kids';
    }

    getLang() {
        return document.querySelector('input[name="lang"]:checked')?.value || 'en';
    }


    async generate() {
        if (!this.selectedKeyword) return;

        document.getElementById('loading').classList.add('active');
        document.getElementById('result').innerHTML = '';

        try {
            const res = await fetch('/api/generate-story', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    keywords: [this.selectedKeyword],
                    age_group: this.getAge(),
                    language: this.getLang()
                })
            });

            const data = await res.json();
            if (data.success) {
                this.currentStory = data.story;
                this.showStory(data.story);
            } else {
                throw new Error(data.error);
            }
        } catch (err) {
            document.getElementById('result').innerHTML = `
                <div style="padding:40px;text-align:center;">
                    <h3 style="color:#ff6b35;">❌ Error</h3>
                    <p style="color:#666;">${err.message}</p>
                </div>`;
        } finally {
            document.getElementById('loading').classList.remove('active');
        }
    }

    async translateTo(lang) {
        // Update radio button
        const radio = document.querySelector(`input[name="lang"][value="${lang}"]`);
        if (radio) radio.checked = true;
        
        // Regenerate with new language
        await this.generate();
    }

    showStory(story) {
        const currentLang = this.getLang();
        
        let html = `
            <div class="story-head">
                <h2>${story.title}</h2>
                <div class="meta-row">
                    <div class="meta-item">📍 ${story.region}</div>
                    <div class="meta-item">⏰ ${story.era}</div>
                    <div class="meta-item">🎯 ${story.age_group}</div>
                    <div class="meta-item">📖 ${story.total_pages} pages</div>
                    <div class="meta-item">🌐 ${this.languages[currentLang]}</div>
                </div>
                <div class="translate-section">
                    <span class="translate-label">🌐 Translate:</span>
                    <div class="translate-btns">
                        <button class="trans-btn ${currentLang === 'en' ? 'active' : ''}" onclick="app.translateTo('en')">English</button>
                        <button class="trans-btn ${currentLang === 'ta' ? 'active' : ''}" onclick="app.translateTo('ta')">தமிழ்</button>
                        <button class="trans-btn ${currentLang === 'hi' ? 'active' : ''}" onclick="app.translateTo('hi')">हिंदी</button>
                        <button class="trans-btn ${currentLang === 'te' ? 'active' : ''}" onclick="app.translateTo('te')">తెలుగు</button>
                        <button class="trans-btn ${currentLang === 'ml' ? 'active' : ''}" onclick="app.translateTo('ml')">മലയാളം</button>
                        <button class="trans-btn ${currentLang === 'kn' ? 'active' : ''}" onclick="app.translateTo('kn')">ಕನ್ನಡ</button>
                        <button class="trans-btn ${currentLang === 'ur' ? 'active' : ''}" onclick="app.translateTo('ur')">اردو</button>
                    </div>
                </div>
            </div>
            <div class="pages-container">`;

        story.pages.forEach(p => {
            html += `
                <div class="page-card">
                    <div class="page-head">
                        <span>📖 Page ${p.page_number}</span>
                        <span>${p.title}</span>
                    </div>
                    <div class="page-body">
                        <p class="page-text">${p.content}</p>
                        <div class="page-info">
                            <span><strong>👥</strong> ${p.characters.join(', ')}</span>
                            <span><strong>📍</strong> ${p.location}</span>
                        </div>
                    </div>
                </div>`;
        });

        html += '</div>';

        if (story.educational_facts?.length) {
            html += `<div class="edu-section"><h3>🎓 Educational Facts</h3>
                ${story.educational_facts.map(f => `<div class="edu-item">${f}</div>`).join('')}</div>`;
        }

        if (story.moral) {
            html += `<div class="edu-section"><h3>💡 Moral</h3><div class="edu-item">${story.moral}</div></div>`;
        }

        document.getElementById('result').innerHTML = html;
        document.getElementById('result').scrollIntoView({ behavior: 'smooth' });
    }
}

// Init
document.addEventListener('DOMContentLoaded', () => { window.app = new StoryApp(); });