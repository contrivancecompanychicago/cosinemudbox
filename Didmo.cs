// Animation Variables
public TextAsset animationJson;
public string animationName;

// Animation Functions
public void LoadAnimation() {
  Didimo.DidimoAnimation animation = Didimo.DidimoAnimation.FromJSONContent(animationName,  animationJson);
  Didimo.AnimationCache.Add(animationName, animation);
}

public void PlayAnimation() {
  didimoComponents.Animator.PlayAnimation(animationName);
}
