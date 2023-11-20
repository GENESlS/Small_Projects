using System.Collections;
using UnityEngine;

public class SpriteAnimator : MonoBehaviour
{
    public Sprite[] sprites; // Assign the 4 sprites in the inspector
    public float animationSpeed = 0.2f; // Time between sprite changes

    private SpriteRenderer spriteRenderer;

    void Start()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            StartCoroutine(AnimateSprite());
        }
    }

    IEnumerator AnimateSprite()
    {
        foreach (Sprite sprite in sprites)
        {
            spriteRenderer.sprite = sprite;
            yield return new WaitForSeconds(animationSpeed);
        }
    }
}
