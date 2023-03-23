import { Component, Input } from '@angular/core';
import { ResIt } from '../res-it';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class ItemComponent {
	@Input() item?: ResIt;
}
