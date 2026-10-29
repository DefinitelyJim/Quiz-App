# Foreman's notes

Running list of things to add as we go. Not in priority order unless stated.
Tick items off and note the milestone they landed in.

## First-time sign-up and onboarding flow

The order a brand-new player should go through:

1. [ ] **Legal agreements** — Terms of Use, Privacy Policy, Cookie Policy, End-User Licence Agreement (EULA). Player must accept before an account is created.
2. [ ] **Sign in / sign up** — choice of own email, phone number, or federated sign-in (e.g. Google / Apple / Microsoft).
3. [ ] **Enter age**
4. [ ] **Gender** (optional)
5. [ ] **Enable push notifications**
6. [ ] **"How the game works"** intro on first sign-in, with light background music.
7. [ ] **Pick 3 favourite quiz genres**
8. [ ] **Pick a favourite decade**
9. [ ] **Test round of 5 questions**, with sound effects.

### Things to bear in mind when we build these

- **Age:** decide a minimum age early. Under-13s (and under-18s generally in the UK) bring extra rules — the ICO's Children's Code — so most apps either set 13+ or design for kids from the start. Age also decides whether some later features (chat, public profiles) are allowed.
- **Gender (optional):** UK GDPR expects us to only collect data we actually use. Worth deciding what it's for (e.g. avatars, stats) before adding it, and including "prefer not to say".
- **Push notifications:** browsers and phones only let you ask once, and many people tap "no" if asked before they've seen the app. Asking right after the test round ("Want to know when a friend challenges you?") usually gets far more yeses. Needs the app installable on the home screen (PWA) to work on iPhone.
- **Background music and sound effects:** browsers block sound until the player has tapped something, so music can't start the instant the page opens. Always include a mute button, remembered between visits.
- **Phone-number sign-in:** needs an SMS provider (costs per text). Email and federated sign-in are free to start with.
- **Federated sign-in:** each provider (Google, Apple, Microsoft) needs a developer account and app registration. Apple sign-in is required on iOS if we offer any other social sign-in in an App Store app.
- **Legal documents:** we can draft them, but they should be checked before real users sign up.
- **Favourite genres and decade:** these should actually change something — e.g. which categories are suggested first, or a decade-themed question pack — or they're just extra taps.

## General

- [ ] **Smartphone friendly** — proper mobile-first pass on every screen (big tap targets, one-handed play, no awkward scrolling mid-question). Pairs naturally with making the app installable (PWA).
