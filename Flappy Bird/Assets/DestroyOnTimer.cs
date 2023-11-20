using UnityEngine;

public class DestroyOnTimer : MonoBehaviour
{
    public float timer = 5f; // Set this to the number of seconds you want to wait before destroying the object

    void Start()
    {
        Destroy(gameObject, timer);
    }
}
